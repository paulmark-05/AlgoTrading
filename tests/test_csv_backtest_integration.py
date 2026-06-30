from decimal import Decimal
from pathlib import Path

from broker.paper_broker import PaperBroker
from data.csv_feed import CSVFeed
from engine.backtest_engine import BacktestEngine
from engine.strategy_engine import StrategyEngine
from engine.trading_engine import TradingEngine
from strategy.manager import StrategyManager
from strategy.reference.noop_strategy import NoOpStrategy


def test_csv_to_backtest_engine_noop_strategy():

    csv_path = Path("tests/data/sample.csv")

    feed = CSVFeed(csv_path)
    data = feed.load()

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

    processed = backtest.run(
        strategy_name="NoOpStrategy",
        symbol="NIFTY",
        data=data,
        quantity=10,
    )

    assert processed == len(data)
    assert len(broker.order_book) == 0
    assert len(broker.trade_book) == 0
    assert broker.cash == Decimal("100000")