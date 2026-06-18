import pandas as pd

from indicators.adx import ADXIndicator


df = pd.read_parquet(
    "data/processed/nifty/NIFTY_5M.parquet"
)

df = ADXIndicator.calculate(
    df,
    length=14
)

print(
    df[
        [
            "date",
            "close",
            "adx_14"
        ]
    ].tail(10)
)