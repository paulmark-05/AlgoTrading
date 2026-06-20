import pandas as pd

from indicators.base_indicator import BaseIndicator


class SMA(BaseIndicator):

    def __init__(self, period=20):
        self.period = period

    def calculate(self, data):

        return data["close"].rolling(self.period).mean()