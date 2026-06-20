from indicators.base_indicator import BaseIndicator
from indicators.atr import ATR


class SuperTrend(BaseIndicator):

    def __init__(
        self,
        period=10,
        multiplier=3
    ):

        self.multiplier = multiplier
        self.atr = ATR(period)

    def calculate(self, data):

        atr = self.atr.calculate(data)

        hl2 = (
            data["high"] +
            data["low"]
        ) / 2

        upper = hl2 + self.multiplier * atr
        lower = hl2 - self.multiplier * atr

        return {
            "upper_band": upper,
            "lower_band": lower
        }