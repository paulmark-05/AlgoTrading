from __future__ import annotations

import pandas as pd

from indicators.base_indicator import BaseIndicator


class ATR(BaseIndicator):

    def __init__(self, period: int = 14) -> None:

        if period <= 0:
            raise ValueError("ATR period must be positive.")

        self.period = period

    @property
    def name(self) -> str:
        return f"ATR_{self.period}"

    def calculate(
        self,
        data: pd.DataFrame,
    ) -> pd.Series:

        required = {"high", "low", "close"}
        missing = required - set(data.columns)

        if missing:
            raise ValueError(
                f"Data missing columns: {sorted(missing)}"
            )

        high_low = data["high"] - data["low"]

        high_prev_close = (
            data["high"] - data["close"].shift(1)
        ).abs()

        low_prev_close = (
            data["low"] - data["close"].shift(1)
        ).abs()

        true_range = pd.concat(
            [
                high_low,
                high_prev_close,
                low_prev_close,
            ],
            axis=1,
        ).max(axis=1)

        return true_range.rolling(
            window=self.period
        ).mean()