from decimal import Decimal
from pathlib import Path

from app.builder import ApplicationBuilder
from app.runner import BacktestRunner
from config.trading_config import TradingConfig
from engine.backtest_result import BacktestResult
from strategy.manager import StrategyManager
from strategy.reference.noop_strategy import NoOpStrategy


def test_backtest_runner_runs_csv():

    config = TradingConfig(
        symbol="NIFTY",
        initial_cash=Decimal("100000"),
        quantity=10,
        max_drawdown=Decimal("5000"),
    )

    manager = StrategyManager()
    manager.add(
        NoOpStrategy(
            symbol="NIFTY"
        )
    )

    app = ApplicationBuilder.build_backtest_application(
        config=config,
        strategy_manager=manager,
    )

    runner = BacktestRunner(
        application=app,
    )

    result = runner.run_csv(
        Path("tests/data/sample.csv")
    )

    assert isinstance(result, BacktestResult)
    assert result.bars_processed == 3
    assert len(result.performance) == 3