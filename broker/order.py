"""
Order model.

Represents an order submitted to the broker.
Supports market, limit, stop and stop-limit orders,
including partial fills and execution history.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from decimal import Decimal
from enum import Enum
from typing import Optional
from uuid import uuid4

class OrderSide(Enum):
    BUY = "BUY"
    SELL = "SELL"


class OrderType(Enum):
    MARKET = "MARKET"
    LIMIT = "LIMIT"
    STOP = "STOP"
    STOP_LIMIT = "STOP_LIMIT"


class OrderStatus(Enum):
    PENDING = "PENDING"
    ACCEPTED = "ACCEPTED"
    PARTIALLY_FILLED = "PARTIALLY_FILLED"
    FILLED = "FILLED"
    CANCELLED = "CANCELLED"
    REJECTED = "REJECTED"


@dataclass(slots=True)
class Execution:
    """
    Represents a single execution (fill) for an order.
    """

    quantity: int
    price: Decimal
    commission: Decimal
    timestamp: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )


@dataclass(slots=True)
class Order:
    """
    Broker order.

    An order may receive multiple executions before being
    completely filled.
    """

    symbol: str

    side: OrderSide

    quantity: int

    order_type: OrderType

    order_id: str = field(
        default_factory=lambda: uuid4().hex
    )

    price: Optional[Decimal] = None

    stop_price: Optional[Decimal] = None

    time_in_force: str = "DAY"

    strategy_id: Optional[str] = None

    created_time: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    submitted_time: Optional[datetime] = None

    accepted_time: Optional[datetime] = None

    filled_time: Optional[datetime] = None

    cancelled_time: Optional[datetime] = None

    rejected_time: Optional[datetime] = None

    rejection_reason: Optional[str] = None

    status: OrderStatus = OrderStatus.PENDING

    filled_quantity: int = 0

    average_price: Decimal = field(
        default_factory=lambda: Decimal("0")
    )

    commission: Decimal = field(
        default_factory=lambda: Decimal("0")
    )

    executions: list[Execution] = field(
        default_factory=list
    )

    metadata: dict = field(
        default_factory=dict
    )

    def __post_init__(self) -> None:

        if self.quantity <= 0:
            raise ValueError(
                "Quantity must be positive."
            )

        if (
            self.order_type == OrderType.LIMIT
            and self.price is None
        ):
            raise ValueError(
                "Limit orders require a limit price."
            )

        if (
            self.order_type == OrderType.STOP
            and self.stop_price is None
        ):
            raise ValueError(
                "Stop orders require a stop price."
            )

        if (
            self.order_type == OrderType.STOP_LIMIT
        ):
            if self.price is None:
                raise ValueError(
                    "Stop-limit orders require a limit price."
                )

            if self.stop_price is None:
                raise ValueError(
                    "Stop-limit orders require a stop price."
                )

        if self.price is not None:
            self.price = Decimal(self.price)

            if self.price <= 0:
                raise ValueError(
                    "Limit price must be positive."
                )

        if self.stop_price is not None:
            self.stop_price = Decimal(
                self.stop_price
            )

            if self.stop_price <= 0:
                raise ValueError(
                    "Stop price must be positive."
                )

    @property
    def remaining_quantity(self) -> int:
        """
        Shares remaining to be executed.
        """
        return self.quantity - self.filled_quantity

    @property
    def fill_ratio(self) -> float:
        """
        Percentage filled.
        """
        return self.filled_quantity / self.quantity

    @property
    def execution_count(self) -> int:
        """
        Number of executions received.
        """
        return len(self.executions)

    @property
    def total_value(self) -> Decimal:
        """
        Dollar value executed using VWAP.
        """
        return (
            self.average_price
            * Decimal(self.filled_quantity)
        )

    @property
    def remaining_value(self) -> Decimal:
        """
        Remaining order value using limit price
        when available.
        """
        if self.price is None:
            return Decimal("0")

        return (
            self.price
            * Decimal(self.remaining_quantity)
        )

    @property
    def has_executions(self) -> bool:
        """
        True if at least one execution exists.
        """
        return bool(self.executions)

    @property
    def last_execution(self) -> Execution | None:
        """
        Most recent execution.
        """
        if not self.executions:
            return None

        return self.executions[-1]

    @property
    def is_open(self) -> bool:
        """
        Order can still receive executions.
        """
        return self.status in (
            OrderStatus.PENDING,
            OrderStatus.ACCEPTED,
            OrderStatus.PARTIALLY_FILLED,
        )

    @property
    def is_closed(self) -> bool:
        """
        Order can no longer receive executions.
        """
        return self.status in (
            OrderStatus.FILLED,
            OrderStatus.CANCELLED,
            OrderStatus.REJECTED,
        )

    @property
    def is_active(self) -> bool:
        """
        Broker considers the order active.
        """
        return self.is_open

    @property
    def is_filled(self) -> bool:
        return self.status == OrderStatus.FILLED

    @property
    def is_cancelled(self) -> bool:
        return self.status == OrderStatus.CANCELLED

    @property
    def is_rejected(self) -> bool:
        return self.status == OrderStatus.REJECTED

    @property
    def is_partially_filled(self) -> bool:
        return (
            self.status
            == OrderStatus.PARTIALLY_FILLED
        )

    def accept(self) -> None:
        """
        Broker accepts the order.
        """
        if self.status != OrderStatus.PENDING:
            raise RuntimeError(
                "Only pending orders may be accepted."
            )

        self.status = OrderStatus.ACCEPTED
        self.accepted_time = datetime.now(
            timezone.utc
        )

    def add_execution(
        self,
        quantity: int,
        price: Decimal,
        commission: Decimal,
    ) -> None:
        """
        Record an execution (fill).

        Supports multiple partial fills while maintaining a
        volume-weighted average execution price (VWAP).
        """

        if self.is_closed:
            raise RuntimeError(
                "Cannot execute a closed order."
            )

        if quantity <= 0:
            raise ValueError(
                "Execution quantity must be positive."
            )

        if quantity > self.remaining_quantity:
            raise ValueError(
                "Execution exceeds remaining quantity."
            )

        price = Decimal(price)
        if price <= 0:
            raise ValueError(
                "Execution price must be positive."
            )
        commission = Decimal(commission)
        if commission < 0:
            raise ValueError(
                "Commission cannot be negative."
            )
        previous_value = (
            self.average_price
            * Decimal(self.filled_quantity)
        )

        execution_value = (
            price
            * Decimal(quantity)
        )

        new_quantity = (
            self.filled_quantity
            + quantity
        )

        self.average_price = (
            previous_value
            + execution_value
        ) / Decimal(new_quantity)

        self.filled_quantity = new_quantity
        self.commission += commission

        self.executions.append(
            Execution(
                quantity=quantity,
                price=price,
                commission=commission,
            )
        )

        if self.filled_quantity == self.quantity:

            self.status = OrderStatus.FILLED
            self.filled_time = datetime.now(
                timezone.utc
            )

        else:

            self.status = (
                OrderStatus.PARTIALLY_FILLED
            )

    def mark_filled(
        self,
        average_price: Decimal,
        commission: Decimal,
    ) -> None:
        """
        Compatibility helper for brokers that execute the
        entire remaining quantity in a single fill.
        """

        self.add_execution(
            quantity=self.remaining_quantity,
            price=average_price,
            commission=commission,
        )

    def mark_partially_filled(
        self,
        quantity: int,
        price: Decimal,
        commission: Decimal,
    ) -> None:
        """
        Backwards-compatible wrapper.
        """

        self.add_execution(
            quantity=quantity,
            price=price,
            commission=commission,
        )

    def reset_fills(self) -> None:
        """
        Clear all executions.

        Mainly intended for testing.
        """

        if self.is_closed:
            raise RuntimeError(
                "Cannot reset a closed order."
            )

        self.executions.clear()

        self.filled_quantity = 0
        self.average_price = Decimal("0")
        self.commission = Decimal("0")

        self.status = OrderStatus.PENDING
        self.accepted_time = None
        self.filled_time = None

    def cancel(self) -> None:
        """
        Cancel an open order.
        """

        if self.is_closed:
            raise RuntimeError(
                "Cannot cancel a closed order."
            )

        self.status = OrderStatus.CANCELLED
        self.cancelled_time = datetime.now(
            timezone.utc
        )

    def reject(
        self,
        reason: str,
    ) -> None:
        """
        Reject an order before execution.
        """

        if self.status != OrderStatus.PENDING:
            raise RuntimeError(
            "Only pending orders may be rejected."
            )

        self.status = OrderStatus.REJECTED
        self.rejected_time = datetime.now(
            timezone.utc
        )
        self.rejection_reason = reason

    def __repr__(self) -> str:

        return (
            "Order("
            f"id={self.order_id}, "
            f"symbol={self.symbol}, "
            f"side={self.side.value}, "
            f"type={self.order_type.value}, "
            f"status={self.status.value}, "
            f"filled={self.filled_quantity}/{self.quantity}, "
            f"avg_price={self.average_price}"
            ")"
        )   

    @property
    def fully_filled(self) -> bool:
        return self.filled_quantity == self.quantity

    @property
    def remaining_percent(self) -> float:
        return self.remaining_quantity / self.quantity

    @property
    def filled_percent(self) -> float:
        return self.filled_quantity / self.quantity