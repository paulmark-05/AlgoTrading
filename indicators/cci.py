from indicators.base_indicator import BaseIndicator


class CCI(BaseIndicator):

    def __init__(self, period=20):

        self.period = period

    def calculate(self, data):

        tp = (
            data["high"] +
            data["low"] +
            data["close"]
        ) / 3

        sma = tp.rolling(self.period).mean()

        md = (
            tp - sma
        ).abs().rolling(self.period).mean()

        cci = (
            tp - sma
        ) / (0.015 * md)

        return cci