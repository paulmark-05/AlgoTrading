import pandas as pd

from indicators.indicator_manager import IndicatorManager

from strategy.nifty_5m_bazooka.filters import BazookaFilters


df = pd.read_parquet(
    "data/processed/nifty/NIFTY_5M.parquet"
)

df = IndicatorManager.calculate_all(df)

row = df.iloc[-1]

print(
    "ADX Bullish:",
    BazookaFilters.adx_bullish(row)
)

print(
    "RSI Bullish:",
    BazookaFilters.rsi_bullish(row)
)

print(
    "SAR Bullish:",
    BazookaFilters.sar_bullish(row)
)

print(
    "EMA Bullish:",
    BazookaFilters.ema_bullish(row)
)

print(
    "MACD Bullish:",
    BazookaFilters.macd_bullish(row)
)

print(
    "Histogram Bullish:",
    BazookaFilters.histogram_bullish(row)
)