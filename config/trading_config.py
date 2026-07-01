from __future__ import annotations

from dataclasses import dataclass
from datetime import time
from decimal import Decimal


@dataclass(frozen=True, slots=True)
class TradingConfig:
    symbol: str
    initial_cash: Decimal
    quantity: int

    max_drawdown: Decimal

    session_start: time = time(9, 25)
    session_end: time = time(15, 10)

    def __post_init__(self) -> None:

        symbol = self.symbol.upper().strip()

        if not symbol:
            raise ValueError(
                "Symbol cannot be empty."
            )

        if self.initial_cash <= 0:
            raise ValueError(
                "Initial cash must be positive."
            )

        if self.quantity <= 0:
            raise ValueError(
                "Quantity must be positive."
            )

        if self.max_drawdown <= 0:
            raise ValueError(
                "Max drawdown must be positive."
            )

        if self.session_start >= self.session_end:
            raise ValueError(
                "Session start must be before session end."
            )

        object.__setattr__(
            self,
            "symbol",
            symbol,
        )