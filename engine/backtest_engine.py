from __future__ import annotations

import pandas as pd

from analytics.performance_tracker import PerformanceTracker
from engine.backtest_result import BacktestResult
from engine.event_bus import EventBus
from engine.event_loop import EventLoop
from engine.performance_recorder import PerformanceRecorder
from engine.replay_engine import ReplayEngine
from engine.trading_engine import TradingEngine


class BacktestEngine:

    def __init__(
        self,
        trading_engine: TradingEngine,
    ) -> None:

        self.trading_engine = trading_engine

        self.event_bus = EventBus()

        self.performance_tracker = PerformanceTracker()

        self.performance_recorder = PerformanceRecorder(
            tracker=self.performance_tracker,
        )

        self.replay_engine = ReplayEngine(
            event_bus=self.event_bus,
        )

        self.event_loop = EventLoop(
            event_bus=self.event_bus,
            trading_engine=trading_engine,
            performance_recorder=self.performance_recorder,
        )

    def run(
        self,
        *,
        strategy_name: str,
        symbol: str,
        data: pd.DataFrame,
        quantity: int,
    ) -> BacktestResult:

        self.replay_engine.replay(
            symbol=symbol,
            data=data,
        )

        bars_processed = self.event_loop.run(
            strategy_name=strategy_name,
            quantity=quantity,
        )

        return BacktestResult(
            bars_processed=bars_processed,
            broker=self.trading_engine.broker,
            performance=self.performance_tracker,
        )