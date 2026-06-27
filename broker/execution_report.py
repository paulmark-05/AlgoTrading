"""
execution_report.py

Represents the result of processing an order.

Every order submitted to the broker should produce exactly one
ExecutionReport describing what happened.

This closely follows institutional OMS/FIX execution reports.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from decimal import Decimal
from typing import Any

from enum import Enum

class ExecutionType(str, Enum):
    FILL = "fill"
    PARTIAL_FILL = "partial_fill"
    CANCEL = "cancel"
    REJECT = "reject"

@dataclass(slots=True)
class ExecutionReport:
    """
    Represents a single broker execution event.

    One report == one broker event.

    Partial fills therefore generate multiple reports.
    """

    order_id: str

    symbol: str

    side: str

    quantity: int

    price: Decimal

    commission: Decimal

    execution_type: ExecutionType

    timestamp: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    execution_id: str | None = None

    broker_order_id: str | None = None

    exchange: str | None = None

    liquidity: str | None = None

    notes: str | None = None

    # ---------------------------------------------------------
    # Convenience Properties
    # ---------------------------------------------------------

    @property
    def gross_value(self) -> Decimal:
        return (
            self.price
            * Decimal(self.quantity)
        )

    @property
    def net_value(self) -> Decimal:
        return (
            self.gross_value
            + self.commission
        )

    @property
    def is_fill(self) -> bool:
        return (
            self.execution_type
            == ExecutionType.FILL
        )

    @property
    def is_partial_fill(self) -> bool:
        return (
            self.execution_type
            == ExecutionType.PARTIAL_FILL
        )

    @property
    def is_cancel(self) -> bool:
        return (
            self.execution_type
            == ExecutionType.CANCEL
        )

    @property
    def is_reject(self) -> bool:
        return (
            self.execution_type
            == ExecutionType.REJECT
        )    
    
    def to_dict(self) -> dict[str, Any]:

        return {
            "order_id": self.order_id,
            "symbol": self.symbol,
            "side": self.side,
            "quantity": self.quantity,
            "price": str(self.price),
            "commission": str(self.commission),
            "execution_type": self.execution_type.value,
            "timestamp": self.timestamp.isoformat(),
            "execution_id": self.execution_id,
            "broker_order_id": self.broker_order_id,
            "exchange": self.exchange,
            "liquidity": self.liquidity,
            "notes": self.notes,
        }
    
    @classmethod
    def from_dict(
        cls,
        data: dict[str, Any],
    ) -> "ExecutionReport":

        return cls(
            order_id=data["order_id"],
            symbol=data["symbol"],
            side=data["side"],
            quantity=data["quantity"],
            price=Decimal(data["price"]),
            commission=Decimal(data["commission"]),
            execution_type=ExecutionType(
                data["execution_type"]
            ),
            timestamp=datetime.fromisoformat(
                data["timestamp"]
            ),
            execution_id=data.get("execution_id"),
            broker_order_id=data.get("broker_order_id"),
            exchange=data.get("exchange"),
            liquidity=data.get("liquidity"),
            notes=data.get("notes"),
        )

    def __repr__(self) -> str:

        return (
            "ExecutionReport("
            f"{self.symbol} "
            f"{self.side} "
            f"{self.quantity}@{self.price} "
            f"{self.execution_type.value}"
            ")"
        )