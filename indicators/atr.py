import pandas as pd

from indicators.base_indicator import BaseIndicator


class ATR(BaseIndicator):

    def __init__(self, period=14):
        self.period = period

    def calculate(self, data):

        high = data["high"]
        low = data["low"]
        close = data["close"]

        tr1 = high - low
        tr2 = (high - close.shift()).abs()
        tr3 = (low - close.shift()).abs()

        tr = pd.concat(
            [tr1, tr2, tr3],
            axis=1
        ).max(axis=1)

        atr = tr.rolling(self.period).mean()

        return atr