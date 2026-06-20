from indicators.base_indicator import BaseIndicator


class VWAP(BaseIndicator):

    def calculate(self, data):

        typical_price = (
            data["high"] +
            data["low"] +
            data["close"]
        ) / 3

        cumulative_tp_vol = (
            typical_price *
            data["volume"]
        ).cumsum()

        cumulative_volume = (
            data["volume"]
        ).cumsum()

        return cumulative_tp_vol / cumulative_volume