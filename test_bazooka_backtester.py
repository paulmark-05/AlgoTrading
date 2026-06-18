import pandas as pd

from backtest.bazooka_backtester import BazookaBacktester

df = pd.read_parquet(
    "data/processed/nifty/NIFTY_5M.parquet"
)

engine = BazookaBacktester()

result = engine.run(df)

print(result)