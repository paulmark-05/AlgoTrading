from __future__ import annotations

import pandas as pd

from indicators.base_indicator import BaseIndicator


class VWAP(BaseIndicator):

    @property
    def name(self) -> str:
        return "VWAP"

    def calculate(
        self,
        data: pd.DataFrame,
    ) -> pd.Series:

        required = {
            "high",
            "low",
            "close",
            "volume",
        }

        missing = required - set(data.columns)

        if missing:
            raise ValueError(
                f"Data missing columns: {sorted(missing)}"
            )

        typical_price = (
            data["high"]
            + data["low"]
            + data["close"]
        ) / 3

        cumulative_pv = (
            typical_price
            * data["volume"]
        ).cumsum()

        cumulative_volume = data["volume"].cumsum()

        return cumulative_pv / cumulative_volume