from decimal import Decimal

from config.factory import ConfigFactory
from config.trading_config import TradingConfig
from risk.risk_engine import RiskEngine
from broker.paper_broker import PaperBroker
from engine.trading_engine import TradingEngine
from strategy.manager import StrategyManager
from strategy.reference.noop_strategy import NoOpStrategy
from engine.backtest_engine import BacktestEngine

def test_create_risk_engine_from_config():

    config = TradingConfig(
        symbol="NIFTY",
        initial_cash=Decimal("100000"),
        quantity=10,
        max_drawdown=Decimal("5000"),
    )

    risk_engine = ConfigFactory.create_risk_engine(
        config
    )

def test_create_paper_broker_from_config():

    config = TradingConfig(
        symbol="NIFTY",
        initial_cash=Decimal("100000"),
        quantity=10,
        max_drawdown=Decimal("5000"),
    )

    broker = ConfigFactory.create_paper_broker(
        config
    )

def test_create_trading_engine_from_config():

    config = TradingConfig(
        symbol="NIFTY",
        initial_cash=Decimal("100000"),
        quantity=10,
        max_drawdown=Decimal("5000"),
    )

    strategy_manager = StrategyManager()
    strategy_manager.add(
        NoOpStrategy(
            symbol="NIFTY"
        )
    )

    engine = ConfigFactory.create_trading_engine(
        config=config,
        strategy_manager=strategy_manager,
    )

def test_create_backtest_engine_from_config():

    config = TradingConfig(
        symbol="NIFTY",
        initial_cash=Decimal("100000"),
        quantity=10,
        max_drawdown=Decimal("5000"),
    )

    strategy_manager = StrategyManager()
    strategy_manager.add(
        NoOpStrategy(
            symbol="NIFTY"
        )
    )

    backtest = ConfigFactory.create_backtest_engine(
        config=config,
        strategy_manager=strategy_manager,
    )

    assert isinstance(backtest, BacktestEngine)
    assert backtest.trading_engine.broker.cash == Decimal("100000")
    
    