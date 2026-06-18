import pandas as pd

from indicators.ema import EMAIndicator
from indicators.rsi import RSIIndicator
from indicators.macd import MACDIndicator

df = pd.read_parquet(
    "data/processed/nifty/NIFTY_5M.parquet"
)

df = EMAIndicator.calculate(df, 20)

df = RSIIndicator.calculate(df, 14)

df = MACDIndicator.calculate(df)

print(
    df[
        [
            "date",
            "close",
            "ema_20",
            "rsi_14",
            "macd",
            "macd_signal",
            "macd_histogram"
        ]
    ].tail(10)
)