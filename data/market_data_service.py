from pathlib import Path

import pandas as pd

class MarketDataService:


    RAW_DATA = (

        Path(
            "data/raw/nifty/NIFTY 50_minute.csv"
        )

    )

    PROCESSED_DATA = (

        Path(
            "data/processed/nifty/NIFTY_5M.parquet"
        )

    )

    @staticmethod
    def load_raw():

        return pd.read_csv(

            MarketDataService.RAW_DATA

        )

    @staticmethod
    def load_processed():

        return pd.read_parquet(

            MarketDataService.PROCESSED_DATA

        )

    @staticmethod
    def latest_candle(df):

        return df.iloc[-1]

    @staticmethod
    def previous_candle(df):

        return df.iloc[-2]

    @staticmethod
    def last_n_candles(

        df,

        n

    ):

        return df.tail(n)

    @staticmethod
    def candle_count(df):

        return len(df)

