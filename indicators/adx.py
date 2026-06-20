from indicators.base_indicator import BaseIndicator
from indicators.dmi import DMI


class ADX(BaseIndicator):

    def __init__(self, period=14):

        self.period = period
        self.dmi = DMI(period)

    def calculate(self, data):

        result = self.dmi.calculate(data)

        plus_di = result["plus_di"]
        minus_di = result["minus_di"]

        dx = (
            (
                (plus_di - minus_di).abs()
            ) /
            (
                plus_di + minus_di
            )
        ) * 100

        adx = dx.rolling(self.period).mean()

        return adx