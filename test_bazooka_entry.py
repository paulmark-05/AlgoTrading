import pandas as pd

from indicators.indicator_manager import IndicatorManager

from strategy.nifty_5m_bazooka.entries import BazookaEntries


df = pd.read_parquet(
    "data/processed/nifty/NIFTY_5M.parquet"
)

df = IndicatorManager.calculate_all(df)

current_row = df.iloc[-1]
previous_row = df.iloc[-2]

print(
    "LONG:",
    BazookaEntries.long_entry(
        current_row,
        previous_row
    )
)

print(
    "SHORT:",
    BazookaEntries.short_entry(
        current_row,
        previous_row
    )
)