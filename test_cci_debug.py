import pandas as pd
import pandas_ta as ta

df = pd.read_parquet(
    "data/processed/nifty/NIFTY_5M.parquet"
)

print(df[["high", "low", "close"]].tail(10))

cci = ta.cci(
    high=df["high"],
    low=df["low"],
    close=df["close"],
    length=20
)

print(cci.tail(10))