from __future__ import annotations

from engine.event import MarketEvent
from engine.event_bus import EventBus
from engine.trading_engine import TradingEngine


class EventLoop:
    """
    Consumes MarketEvents from the EventBus
    and forwards them to the TradingEngine.
    """

    def __init__(
        self,
        event_bus: EventBus,
        trading_engine: TradingEngine,
    ) -> None:

        self.event_bus = event_bus
        self.trading_engine = trading_engine

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

            market_price = event.data.iloc[-1]["close"]

            self.trading_engine.run_once(
                strategy_name=strategy_name,
                symbol=event.symbol,
                data=event.data,
                quantity=quantity,
                market_price=market_price,
            )

            processed += 1

        return processed
        