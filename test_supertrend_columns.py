import pandas as pd
import pandas_ta as ta

df = pd.read_parquet(
    "data/processed/nifty/NIFTY_5M.parquet"
)

st = ta.supertrend(
    high=df["high"],
    low=df["low"],
    close=df["close"],
    length=10,
    multiplier=3
)

print(st.columns)
print(st.tail())