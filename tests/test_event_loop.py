from decimal import Decimal

import pandas as pd

from broker.paper_broker import PaperBroker
from engine.event import MarketEvent
from engine.event_bus import EventBus
from engine.event_loop import EventLoop
from engine.strategy_engine import StrategyEngine
from engine.trading_engine import TradingEngine
from strategy.manager import StrategyManager
from strategy.reference.noop_strategy import NoOpStrategy


def sample_df():

    return pd.DataFrame(
        {
            "datetime": ["2025-01-01"],
            "open": [100],
            "high": [110],
            "low": [90],
            "close": [105],
            "volume": [1000],
        }
    )


def test_event_loop_processes_all_events():

    manager = StrategyManager()
    manager.add(
        NoOpStrategy(symbol="NIFTY")
    )

    strategy_engine = StrategyEngine(
        strategy_manager=manager,
    )

    broker = PaperBroker(
        initial_cash=Decimal("100000")
    )

    trading_engine = TradingEngine(
        strategy_engine=strategy_engine,
        broker=broker,
    )

    bus = EventBus()

    bus.publish(
        MarketEvent(
            symbol="NIFTY",
            data=sample_df(),
        )
    )

    bus.publish(
        MarketEvent(
            symbol="NIFTY",
            data=sample_df(),
        )
    )

    loop = EventLoop(
        event_bus=bus,
        trading_engine=trading_engine,
    )

    processed = loop.run(
        strategy_name="NoOpStrategy",
        quantity=10,
    )

    assert processed == 2
    assert bus.empty()


def test_empty_bus_returns_zero():

    manager = StrategyManager()
    manager.add(
        NoOpStrategy(symbol="NIFTY")
    )

    strategy_engine = StrategyEngine(
        strategy_manager=manager,
    )

    broker = PaperBroker(
        initial_cash=Decimal("100000")
    )

    trading_engine = TradingEngine(
        strategy_engine=strategy_engine,
        broker=broker,
    )

    bus = EventBus()

    loop = EventLoop(
        event_bus=bus,
        trading_engine=trading_engine,
    )

    assert loop.run(
        strategy_name="NoOpStrategy",
        quantity=10,
    ) == 0