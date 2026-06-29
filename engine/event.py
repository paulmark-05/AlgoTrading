from __future__ import annotations

from dataclasses import dataclass

import pandas as pd


@dataclass(frozen=True, slots=True)
class MarketEvent:
    symbol: str
    data: pd.DataFrame

    def __post_init__(self) -> None:
        symbol = self.symbol.upper().strip()

        if not symbol:
            raise ValueError("MarketEvent symbol cannot be empty.")

        if self.data.empty:
            raise ValueError("MarketEvent data cannot be empty.")

        object.__setattr__(self, "symbol", symbol)