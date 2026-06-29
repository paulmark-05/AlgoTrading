from __future__ import annotations

import pandas as pd

from indicators.atr import ATR
from indicators.base_indicator import BaseIndicator


class ADX(BaseIndicator):

    def __init__(self, period: int = 14) -> None:

        if period <= 0:
            raise ValueError("ADX period must be positive.")

        self.period = period

    @property
    def name(self) -> str:
        return f"ADX_{self.period}"

    def calculate(
        self,
        data: pd.DataFrame,
    ) -> pd.Series:

        required = {
            "high",
            "low",
            "close",
        }

        missing = required - set(data.columns)

        if missing:
            raise ValueError(
                f"Data missing columns: {sorted(missing)}"
            )

        high = data["high"]
        low = data["low"]

        up_move = high.diff()
        down_move = -low.diff()

        plus_dm = up_move.where(
            (up_move > down_move) & (up_move > 0),
            0.0,
        )

        minus_dm = down_move.where(
            (down_move > up_move) & (down_move > 0),
            0.0,
        )

        atr = ATR(self.period).calculate(data)

        plus_di = (
            100
            * plus_dm.rolling(self.period).sum()
            / atr
        )

        minus_di = (
            100
            * minus_dm.rolling(self.period).sum()
            / atr
        )

        dx = (
            (plus_di - minus_di).abs()
            / (plus_di + minus_di)
        ) * 100

        return dx.rolling(
            self.period
        ).mean()