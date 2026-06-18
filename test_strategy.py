import pandas as pd

from indicators.indicator_manager import IndicatorManager

from strategy.multi_confluence import (
    MultiConfluenceStrategy
)


df = pd.read_parquet(
    "data/processed/nifty/NIFTY_5M.parquet"
)

df = IndicatorManager.calculate_all(df)

strategy = MultiConfluenceStrategy()

last_row = df.iloc[-1]

signal = strategy.generate_signal(
    last_row
)

print(signal)