import pandas as pd

from indicators.ema import (
    EMAIndicator
)

df = pd.read_parquet(
    "data/processed/nifty/NIFTY_5M.parquet"
)

df = EMAIndicator.calculate(
    df,
    length=20
)

print(
    df[
        [
            "date",
            "close",
            "ema_20"
        ]
    ].tail(10)
)