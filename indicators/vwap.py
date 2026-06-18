import pandas as pd


class VWAPIndicator:

    @staticmethod
    def calculate(df):

        typical_price = (
            df["high"] +
            df["low"] +
            df["close"]
        ) / 3

        cumulative_tp_vol = (
            typical_price * df["volume"]
        ).cumsum()

        cumulative_volume = (
            df["volume"]
        ).cumsum()

        df["vwap"] = (
            cumulative_tp_vol /
            cumulative_volume
        )

        return df