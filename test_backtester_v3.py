from backtest.backtester import Backtester

bt = Backtester()

bt.add_trade(
    signal="BUY",
    entry_price=23800,
    exit_price=23840,
    pnl=40,
    result="WIN",
    entry_time="10:00",
    exit_time="10:20"
)

bt.add_trade(
    signal="SELL",
    entry_price=23850,
    exit_price=23870,
    pnl=-20,
    result="LOSS",
    entry_time="11:00",
    exit_time="11:15"
)

print(
    bt.summary()
)