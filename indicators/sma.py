from __future__ import annotations

import pandas as pd

from indicators.base_indicator import BaseIndicator


class SMA(BaseIndicator):

    def __init__(self, period: int) -> None:

        if period <= 0:
            raise ValueError("SMA period must be positive.")

        self.period = period

    @property
    def name(self) -> str:
        return f"SMA_{self.period}"

    def calculate(
        self,
        data: pd.DataFrame,
    ) -> pd.Series:

        if "close" not in data.columns:
            raise ValueError("Data must contain close column.")

        return data["close"].rolling(
            window=self.period
        ).mean()