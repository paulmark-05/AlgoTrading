from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True, slots=True)
class PerformanceSnapshot:
    """
    Represents portfolio performance at a point in time.
    """

    timestamp: object

    cash: Decimal
    market_value: Decimal
    total_value: Decimal

    realized_pnl: Decimal
    unrealized_pnl: Decimal
    total_pnl: Decimal

    def __post_init__(self) -> None:

        values = (
            self.cash,
            self.market_value,
            self.total_value,
            self.realized_pnl,
            self.unrealized_pnl,
            self.total_pnl,
        )

        for value in values:
            if not isinstance(value, Decimal):
                raise TypeError(
                    "All monetary values must be Decimal."
                )