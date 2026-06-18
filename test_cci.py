import pandas as pd

from indicators.cci import CCIIndicator


df = pd.read_parquet(
    "data/processed/nifty/NIFTY_5M.parquet"
)

df = CCIIndicator.calculate(
    df,
    length=20
)

print(
    df[
        [
            "date",
            "close",
            "cci_20"
        ]
    ].tail(10)
)