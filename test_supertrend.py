import pandas as pd

from indicators.supertrend import (
    SupertrendIndicator
)

df = pd.read_parquet(
    "data/processed/nifty/NIFTY_5M.parquet"
)

df = SupertrendIndicator.calculate(
    df,
    length=10,
    multiplier=3
)

print(
    df[
        [
            "date",
            "close",
            "supertrend_10_3",
            "supertrend_direction_10_3"
        ]
    ].tail(10)
)