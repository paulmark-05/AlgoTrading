from __future__ import annotations

from dataclasses import dataclass

from config.trading_config import TradingConfig
from engine.backtest_engine import BacktestEngine


@dataclass(slots=True)
class TradingApplication:
    """
    Root application object.

    Owns the configured trading system.
    """

    config: TradingConfig

    backtest: BacktestEngine