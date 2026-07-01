from __future__ import annotations

from config.trading_config import TradingConfig
from risk.max_drawdown_rule import MaxDrawdownRule
from risk.risk_engine import RiskEngine
from risk.session_time_rule import SessionTimeRule
from broker.paper_broker import PaperBroker
from engine.strategy_engine import StrategyEngine
from engine.trading_engine import TradingEngine
from strategy.manager import StrategyManager
from engine.backtest_engine import BacktestEngine

class ConfigFactory:

    @staticmethod
    def create_risk_engine(
        config: TradingConfig,
    ) -> RiskEngine:

        risk_engine = RiskEngine()

        risk_engine.add_rule(
            MaxDrawdownRule(
                max_drawdown=config.max_drawdown,
            )
        )

        risk_engine.add_rule(
            SessionTimeRule(
                entry_start=config.session_start,
                entry_end=config.session_end,
            )
        )

        return risk_engine
    
    @staticmethod
    def create_paper_broker(
        config: TradingConfig,
    ) -> PaperBroker:

        return PaperBroker(
            initial_cash=config.initial_cash,
        )

    @staticmethod
    def create_trading_engine(
        *,
        config: TradingConfig,
        strategy_manager: StrategyManager,
    ) -> TradingEngine:

        broker = ConfigFactory.create_paper_broker(
            config
        )

        risk_engine = ConfigFactory.create_risk_engine(
            config
        )

        strategy_engine = StrategyEngine(
            strategy_manager=strategy_manager,
        )

        return TradingEngine(
            strategy_engine=strategy_engine,
            broker=broker,
            risk_manager=risk_engine,
        )
    
    @staticmethod
    def create_backtest_engine(
        *,
        config: TradingConfig,
        strategy_manager: StrategyManager,
    ) -> BacktestEngine:

        trading_engine = ConfigFactory.create_trading_engine(
            config=config,
            strategy_manager=strategy_manager,
        )

        return BacktestEngine(
            trading_engine=trading_engine,
        )