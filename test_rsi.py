import pandas as pd

from indicators.ema import EMAIndicator
from indicators.rsi import RSIIndicator

df = pd.read_parquet(
    "data/processed/nifty/NIFTY_5M.parquet"
)

df = EMAIndicator.calculate(
    df,
    length=20
)

df = RSIIndicator.calculate(
    df,
    length=14
)

print(
    df[
        [
            "date",
            "close",
            "ema_20",
            "rsi_14"
        ]
    ].tail(10)
)
