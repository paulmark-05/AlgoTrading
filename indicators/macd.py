from indicators.base_indicator import BaseIndicator


class MACD(BaseIndicator):

    def calculate(self, data):

        ema12 = data["close"].ewm(
            span=12,
            adjust=False
        ).mean()

        ema26 = data["close"].ewm(
            span=26,
            adjust=False
        ).mean()

        macd = ema12 - ema26

        signal = macd.ewm(
            span=9,
            adjust=False
        ).mean()

        histogram = macd - signal

        return {
            "macd": macd,
            "signal": signal,
            "histogram": histogram,
        }