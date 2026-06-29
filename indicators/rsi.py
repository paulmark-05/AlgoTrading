from __future__ import annotations

import pandas as pd

from indicators.base_indicator import BaseIndicator


class RSI(BaseIndicator):

    def __init__(self, period: int = 14) -> None:

        if period <= 0:
            raise ValueError("RSI period must be positive.")

        self.period = period

    @property
    def name(self) -> str:
        return f"RSI_{self.period}"

    def calculate(
        self,
        data: pd.DataFrame,
    ) -> pd.Series:

        if "close" not in data.columns:
            raise ValueError("Data must contain close column.")

        delta = data["close"].diff()

        gain = delta.clip(lower=0)
        loss = -delta.clip(upper=0)

        average_gain = gain.rolling(
            window=self.period
        ).mean()

        average_loss = loss.rolling(
            window=self.period
        ).mean()

        rs = average_gain / average_loss

        return 100 - (
            100 / (1 + rs)
        )