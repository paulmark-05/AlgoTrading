import pandas as pd

df = pd.read_parquet(
    "data/processed/nifty/NIFTY_5M.parquet"
)

print(df["volume"].describe())