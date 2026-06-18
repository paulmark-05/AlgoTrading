import pandas as pd

from indicators.vwap import VWAPIndicator

df = pd.read_parquet(
    "data/processed/nifty/NIFTY_5M.parquet"
)

df = VWAPIndicator.calculate(df)

print(
    df[
        [
            "date",
            "close",
            "vwap"
        ]
    ].tail(10)
)