"""
signal.py

Trading signal model.

A strategy does not place orders directly.
It only emits a Signal.

The engine later converts a Signal into an Order.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from decimal import Decimal
from enum import Enum
from typing import Any


class SignalSide(str, Enum):
    BUY = "BUY"
    SELL = "SELL"
    HOLD = "HOLD"


@dataclass(frozen=True, slots=True)
class Signal:
    """
    Represents a strategy decision.
    """

    symbol: str
    side: SignalSide

    strength: Decimal = Decimal("1")
    price: Decimal | None = None
    reason: str = ""

    metadata: dict[str, Any] = field(
        default_factory=dict
    )

    timestamp: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    def __post_init__(self) -> None:

        symbol = self.symbol.upper().strip()

        if not symbol:
            raise ValueError(
                "Signal symbol cannot be empty."
            )

        object.__setattr__(
            self,
            "symbol",
            symbol,
        )

        strength = Decimal(self.strength)

        if strength < 0:
            raise ValueError(
                "Signal strength cannot be negative."
            )

        object.__setattr__(
            self,
            "strength",
            strength,
        )

        if self.price is not None:

            price = Decimal(self.price)

            if price <= 0:
                raise ValueError(
                    "Signal price must be positive."
                )

            object.__setattr__(
                self,
                "price",
                price,
            )

    @property
    def is_buy(self) -> bool:
        return self.side == SignalSide.BUY

    @property
    def is_sell(self) -> bool:
        return self.side == SignalSide.SELL

    @property
    def is_hold(self) -> bool:
        return self.side == SignalSide.HOLD

    def __repr__(self) -> str:

        return (
            "Signal("
            f"symbol={self.symbol}, "
            f"side={self.side.value}, "
            f"strength={self.strength}, "
            f"price={self.price}, "
            f"reason={self.reason}"
            ")"
        )