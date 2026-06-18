import pandas as pd

from indicators.indicator_manager import (
    IndicatorManager
)

df = pd.read_parquet(
    "data/processed/nifty/NIFTY_5M.parquet"
)

df = IndicatorManager.calculate_all(df)

print(
    df[
        [
            "date",
            "close",
            "ema_5",
            "ema_9",
            "ema_21",
            "ema_54",
            "ema_200",
            "rsi_14",
            "macd",
            "macd_signal",
            "macd_histogram"
        ]
    ].tail(10)
)