import pandas as pd

from indicators.dmi import DMIIndicator

df = pd.read_parquet(
    "data/processed/nifty/NIFTY_5M.parquet"
)

df = DMIIndicator.calculate(df)

print(
    df[
        [
            "date",
            "adx_14",
            "plus_di_14",
            "minus_di_14"
        ]
    ].tail(10)
)