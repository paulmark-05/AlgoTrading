from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

import pandas as pd


@dataclass(frozen=True, slots=True)
class StrategyContext:
    symbol: str
    data: pd.DataFrame
    indicators: dict[str, Any] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        symbol = self.symbol.upper().strip()

        if not symbol:
            raise ValueError("Symbol cannot be empty.")

        if self.data.empty:
            raise ValueError("Market data is empty.")

        object.__setattr__(self, "symbol", symbol)

    @property
    def latest(self):
        return self.data.iloc[-1]

    def indicator(
        self,
        name: str,
    ):
        return self.indicators.get(name)