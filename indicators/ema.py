from __future__ import annotations

import pandas as pd

from indicators.base_indicator import BaseIndicator


class EMA(BaseIndicator):

    def __init__(self, period: int) -> None:

        if period <= 0:
            raise ValueError("EMA period must be positive.")

        self.period = period

    @property
    def name(self) -> str:
        return f"EMA_{self.period}"

    def calculate(
        self,
        data: pd.DataFrame,
    ) -> pd.Series:

        if "close" not in data.columns:
            raise ValueError("Data must contain close column.")

        return data["close"].ewm(
            span=self.period,
            adjust=False,
        ).mean()