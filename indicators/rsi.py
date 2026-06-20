import pandas as pd

from indicators.base_indicator import BaseIndicator


class RSI(BaseIndicator):

    def __init__(self, period=14):
        self.period = period

    def calculate(self, data):

        delta = data["close"].diff()

        gain = delta.clip(lower=0)

        loss = -delta.clip(upper=0)

        avg_gain = gain.rolling(self.period).mean()

        avg_loss = loss.rolling(self.period).mean()

        rs = avg_gain / avg_loss

        return 100 - (100 / (1 + rs))