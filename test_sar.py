import pandas as pd

from indicators.sar import SARIndicator


df = pd.read_parquet(
    "data/processed/nifty/NIFTY_5M.parquet"
)

df = SARIndicator.calculate(df)

print(
    df[
        [
            "date",
            "close",
            "psar"
        ]
    ].tail(10)
)