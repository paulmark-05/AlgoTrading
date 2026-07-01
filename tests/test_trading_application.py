from decimal import Decimal

from app.application import TradingApplication
from config.factory import ConfigFactory
from config.trading_config import TradingConfig
from strategy.manager import StrategyManager
from strategy.reference.noop_strategy import NoOpStrategy


def test_application_creation():

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

    backtest = ConfigFactory.create_backtest_engine(
        config=config,
        strategy_manager=manager,
    )

    app = TradingApplication(
        config=config,
        backtest=backtest,
    )

    assert app.config is config
    assert app.backtest is backtest