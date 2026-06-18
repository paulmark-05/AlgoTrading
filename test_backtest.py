import pandas as pd

from indicators.indicator_manager import IndicatorManager

from strategy.multi_confluence import (
    MultiConfluenceStrategy
)

from backtest.backtester import (
    Backtester
)


df = pd.read_parquet(
    "data/processed/nifty/NIFTY_5M.parquet"
)

df = IndicatorManager.calculate_all(df)

strategy = MultiConfluenceStrategy()

backtester = Backtester()


for _, row in df.tail(500).iterrows():

    signal = strategy.generate_signal(row)

    if signal.signal.value != "HOLD":

        backtester.add_trade(
            signal=signal.signal.value,
            price=signal.price,
            stop_loss=signal.stop_loss,
            timestamp=row["date"]
        )


print(backtester.summary())