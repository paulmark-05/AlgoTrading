import pandas as pd

from indicators.base_indicator import BaseIndicator


class DMI(BaseIndicator):

    def __init__(self, period=14):

        self.period = period

    def calculate(self, data):

        high = data["high"]
        low = data["low"]
        close = data["close"]

        plus_dm = high.diff()

        minus_dm = -low.diff()

        plus_dm = plus_dm.where(
            (plus_dm > minus_dm) & (plus_dm > 0),
            0
        )

        minus_dm = minus_dm.where(
            (minus_dm > plus_dm) & (minus_dm > 0),
            0
        )

        tr1 = high - low
        tr2 = (high - close.shift()).abs()
        tr3 = (low - close.shift()).abs()

        tr = pd.concat(
            [tr1, tr2, tr3],
            axis=1
        ).max(axis=1)

        atr = tr.rolling(self.period).mean()

        plus_di = (
            100 *
            plus_dm.rolling(self.period).mean()
            / atr
        )

        minus_di = (
            100 *
            minus_dm.rolling(self.period).mean()
            / atr
        )

        return {
            "plus_di": plus_di,
            "minus_di": minus_di
        }