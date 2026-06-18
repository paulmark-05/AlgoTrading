import pandas as pd

from strategy.nifty_5m_bazooka.filters import Filters

df = pd.read_parquet(
    "data/processed/nifty/NIFTY_5M.parquet"
)

from indicators.indicator_manager import IndicatorManager

df = IndicatorManager.calculate_all(df)

row = df.iloc[-1]

print("EMA Bullish:", Filters.ema_bullish(row))
print("RSI Bullish:", Filters.rsi_bullish(row))
print("MACD Bullish:", Filters.macd_bullish(row))
print("ADX Strong:", Filters.adx_strong(row))
print("DI Bullish:", Filters.di_bullish(row))