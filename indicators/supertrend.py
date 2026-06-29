from __future__ import annotations

import pandas as pd

from indicators.atr import ATR
from indicators.base_indicator import BaseIndicator


class SuperTrend(BaseIndicator):

    def __init__(
        self,
        period: int = 10,
        multiplier: float = 3.0,
    ) -> None:

        if period <= 0:
            raise ValueError("SuperTrend period must be positive.")

        if multiplier <= 0:
            raise ValueError("SuperTrend multiplier must be positive.")

        self.period = period
        self.multiplier = multiplier

    @property
    def name(self) -> str:
        return f"SUPERTREND_{self.period}_{self.multiplier}"

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

        high = data["high"]
        low = data["low"]
        close = data["close"]

        atr = ATR(self.period).calculate(data)

        hl2 = (high + low) / 2

        upper_band = hl2 + (self.multiplier * atr)
        lower_band = hl2 - (self.multiplier * atr)

        supertrend = pd.Series(
            index=data.index,
            dtype="float64",
        )

        direction_up = True

        for i in range(len(data)):

            if pd.isna(atr.iloc[i]):
                supertrend.iloc[i] = pd.NA
                continue

            if i == 0:
                supertrend.iloc[i] = lower_band.iloc[i]
                continue

            previous_supertrend = supertrend.iloc[i - 1]

            if close.iloc[i] > upper_band.iloc[i - 1]:
                direction_up = True

            elif close.iloc[i] < lower_band.iloc[i - 1]:
                direction_up = False

            if direction_up:
                supertrend.iloc[i] = lower_band.iloc[i]

                if (
                    not pd.isna(previous_supertrend)
                    and supertrend.iloc[i] < previous_supertrend
                ):
                    supertrend.iloc[i] = previous_supertrend

            else:
                supertrend.iloc[i] = upper_band.iloc[i]

                if (
                    not pd.isna(previous_supertrend)
                    and supertrend.iloc[i] > previous_supertrend
                ):
                    supertrend.iloc[i] = previous_supertrend

        return supertrend