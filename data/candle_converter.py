import pandas as pd


class CandleConverter:

    @staticmethod
    def convert_to_5m(df):

        df = df.copy()

        df = df.set_index("date")

        candle_5m = df.resample("5min").agg(
            {
                "open": "first",
                "high": "max",
                "low": "min",
                "close": "last",
                "volume": "sum"
            }
        )

        candle_5m = candle_5m.dropna()

        candle_5m = candle_5m.reset_index()

        return candle_5m