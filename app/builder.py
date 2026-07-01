from __future__ import annotations

from app.application import TradingApplication
from config.factory import ConfigFactory
from config.trading_config import TradingConfig
from strategy.manager import StrategyManager


class ApplicationBuilder:

    @staticmethod
    def build_backtest_application(
        *,
        config: TradingConfig,
        strategy_manager: StrategyManager,
    ) -> TradingApplication:

        backtest = ConfigFactory.create_backtest_engine(
            config=config,
            strategy_manager=strategy_manager,
        )

        return TradingApplication(
            config=config,
            backtest=backtest,
        )