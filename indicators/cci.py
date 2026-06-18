import pandas as pd


class CCIIndicator:

    @staticmethod
    def calculate(df, length=20):

        tp = (
            df["high"] +
            df["low"] +
            df["close"]
        ) / 3

        sma_tp = tp.rolling(length).mean()

        mean_dev = tp.rolling(length).apply(
            lambda x: abs(x - x.mean()).mean(),
            raw=True
        )

        cci = (
            tp - sma_tp
        ) / (
            0.015 * mean_dev
        )

        df[f"cci_{length}"] = cci

        return df