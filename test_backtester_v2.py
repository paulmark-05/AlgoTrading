from backtest.backtester import Backtester

bt = Backtester()

bt.add_trade(

    signal="BUY",

    entry_price=23800,

    stop_loss=23780,

    target=23840,

    exit_price=23840,

    result="WIN",

    pnl=40,

    entry_time="10:00",

    exit_time="10:20"
)

bt.add_trade(

    signal="BUY",

    entry_price=23900,

    stop_loss=23880,

    target=23940,

    exit_price=23880,

    result="LOSS",

    pnl=-20,

    entry_time="11:00",

    exit_time="11:10"
)

print(
    bt.summary()
)