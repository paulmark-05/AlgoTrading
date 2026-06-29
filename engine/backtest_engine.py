from __future__ import annotations

import pandas as pd

from engine.event_bus import EventBus
from engine.event_loop import EventLoop
from engine.replay_engine import ReplayEngine
from engine.trading_engine import TradingEngine


class BacktestEngine:

    def __init__(
        self,
        trading_engine: TradingEngine,
    ) -> None:

        self.event_bus = EventBus()

        self.replay_engine = ReplayEngine(
            event_bus=self.event_bus,
        )

        self.event_loop = EventLoop(
            event_bus=self.event_bus,
            trading_engine=trading_engine,
        )

    def run(
        self,
        *,
        strategy_name: str,
        symbol: str,
        data: pd.DataFrame,
        quantity: int,
    ) -> int:

        self.replay_engine.replay(
            symbol=symbol,
            data=data,
        )

        return self.event_loop.run(
            strategy_name=strategy_name,
            quantity=quantity,
        )