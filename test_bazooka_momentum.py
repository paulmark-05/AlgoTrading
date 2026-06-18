import pandas as pd

from indicators.indicator_manager import IndicatorManager

from strategy.nifty_5m_bazooka.filters import BazookaFilters


df = pd.read_parquet(
    "data/processed/nifty/NIFTY_5M.parquet"
)

df = IndicatorManager.calculate_all(df)

current_row = df.iloc[-1]
previous_row = df.iloc[-2]

print(
    "RSI Rising:",
    BazookaFilters.rsi_rising(
        current_row,
        previous_row
    )
)

print(
    "MACD Diff Rising:",
    BazookaFilters.macd_diff_rising(
        current_row,
        previous_row
    )
)

print(
    "Histogram Rising:",
    BazookaFilters.histogram_rising(
        current_row,
        previous_row
    )
)

print(
    "Plus DI Rising:",
    BazookaFilters.plus_di_rising(
        current_row,
        previous_row
    )
)