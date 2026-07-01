from __future__ import annotations

from engine.event_bus import EventBus
from engine.performance_recorder import PerformanceRecorder
from engine.trading_engine import TradingEngine


class EventLoop:

    def __init__(
        self,
        event_bus: EventBus,
        trading_engine: TradingEngine,
        performance_recorder: PerformanceRecorder | None = None,
    ) -> None:

        self.event_bus = event_bus
        self.trading_engine = trading_engine
        self.performance_recorder = performance_recorder

    def run(
        self,
        *,
        strategy_name: str,
        quantity: int,
    ) -> int:

        processed = 0

        while True:

            event = self.event_bus.next()

            if event is None:
                break

            latest = event.data.iloc[-1]

            market_price = latest["close"]

            self.trading_engine.run_once(
                strategy_name=strategy_name,
                symbol=event.symbol,
                data=event.data,
                quantity=quantity,
                market_price=market_price,
            )

            if self.performance_recorder is not None:

                timestamp = latest["datetime"]

                self.performance_recorder.record(
                    timestamp=timestamp,
                    broker=self.trading_engine.broker,
                )

            processed += 1

        return processed