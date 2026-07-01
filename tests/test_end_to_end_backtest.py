from decimal import Decimal
from pathlib import Path

from app.builder import ApplicationBuilder
from app.runner import BacktestRunner
from config.trading_config import TradingConfig
from strategy.manager import StrategyManager
from strategy.reference.noop_strategy import NoOpStrategy


def test_complete_backtest_pipeline():

    config = TradingConfig(
        symbol="NIFTY",
        initial_cash=Decimal("100000"),
        quantity=10,
        max_drawdown=Decimal("5000"),
    )

    manager = StrategyManager()

    manager.add(
        NoOpStrategy(
            symbol="NIFTY",
        )
    )

    application = (
        ApplicationBuilder.build_backtest_application(
            config=config,
            strategy_manager=manager,
        )
    )

    runner = BacktestRunner(
        application=application,
    )

    result = runner.run_csv(
        Path("tests/data/sample.csv"),
    )

    report = result.report()

    assert result.bars_processed == 3
    assert len(result.performance) == 3

    assert report["snapshots"] == 3
    assert report["closed_trades"] == 0

    broker = result.broker

    assert broker.cash == Decimal("100000")
    assert len(broker.order_book) == 0
    assert len(broker.trade_book) == 0