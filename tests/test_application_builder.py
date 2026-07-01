from decimal import Decimal

from app.application import TradingApplication
from app.builder import ApplicationBuilder
from config.trading_config import TradingConfig
from strategy.manager import StrategyManager
from strategy.reference.noop_strategy import NoOpStrategy


def test_build_backtest_application():

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

    assert isinstance(app, TradingApplication)
    assert app.config is config
    assert app.backtest.trading_engine.broker.cash == Decimal("100000")