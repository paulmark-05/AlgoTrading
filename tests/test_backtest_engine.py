from decimal import Decimal

import pandas as pd

from broker.paper_broker import PaperBroker
from engine.backtest_engine import BacktestEngine
from engine.strategy_engine import StrategyEngine
from engine.trading_engine import TradingEngine
from strategy.manager import StrategyManager
from strategy.reference.noop_strategy import NoOpStrategy


def sample_df():

    return pd.DataFrame(
        {
            "datetime": [
                "2025-01-01",
                "2025-01-02",
                "2025-01-03",
            ],
            "open": [100, 101, 102],
            "high": [110, 111, 112],
            "low": [90, 91, 92],
            "close": [105, 106, 107],
            "volume": [1000, 1100, 1200],
        }
    )


def test_backtest_engine_runs_all_rows():

    manager = StrategyManager()
    manager.add(
        NoOpStrategy(symbol="NIFTY")
    )

    strategy_engine = StrategyEngine(
        strategy_manager=manager,
    )

    broker = PaperBroker(
        initial_cash=Decimal("100000")
    )

    trading_engine = TradingEngine(
        strategy_engine=strategy_engine,
        broker=broker,
    )

    backtest = BacktestEngine(
        trading_engine=trading_engine,
    )

    result = backtest.run(
        strategy_name="NoOpStrategy",
        symbol="NIFTY",
        data=sample_df(),
        quantity=10,
    )

    assert result.bars_processed == 3
    assert len(result.performance) == 3
    assert len(broker.order_book) == 0
    assert len(broker.trade_book) == 0