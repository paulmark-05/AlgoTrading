from decimal import Decimal

import pandas as pd
import pytest

from strategy.base_strategy import BaseStrategy
from strategy.context import StrategyContext
from strategy.manager import StrategyManager
from strategy.signal import Signal, SignalSide


class DummyStrategy(BaseStrategy):

    def generate_signal(
        self,
        context: StrategyContext,
    ) -> Signal:

        return Signal(
            symbol=context.symbol,
            side=SignalSide.HOLD,
            strength=Decimal("1"),
        )


def sample_context():

    data = pd.DataFrame(
        {
            "datetime": ["2025-01-01"],
            "open": [100],
            "high": [110],
            "low": [90],
            "close": [105],
            "volume": [1000],
        }
    )

    return StrategyContext(
        symbol="NIFTY",
        data=data,
    )


def test_new_manager():

    manager = StrategyManager()

    assert len(manager) == 0


def test_add_strategy():

    manager = StrategyManager()
    strategy = DummyStrategy(
        name="Dummy",
        symbol="NIFTY",
    )

    manager.add(strategy)

    assert len(manager) == 1
    assert manager.has("Dummy")


def test_get_strategy():

    manager = StrategyManager()
    strategy = DummyStrategy(
        name="Dummy",
        symbol="NIFTY",
    )

    manager.add(strategy)

    assert manager.get("Dummy") is strategy


def test_missing_strategy_returns_none():

    manager = StrategyManager()

    assert manager.get("Missing") is None


def test_all_strategies():

    manager = StrategyManager()
    strategy = DummyStrategy(
        name="Dummy",
        symbol="NIFTY",
    )

    manager.add(strategy)

    assert manager.all() == [strategy]


def test_evaluate_strategy():

    manager = StrategyManager()
    strategy = DummyStrategy(
        name="Dummy",
        symbol="NIFTY",
    )

    manager.add(strategy)

    signal = manager.evaluate(
        "Dummy",
        sample_context(),
    )

    assert signal.symbol == "NIFTY"
    assert signal.side == SignalSide.HOLD


def test_evaluate_missing_strategy_raises():

    manager = StrategyManager()

    with pytest.raises(ValueError):
        manager.evaluate(
            "Missing",
            sample_context(),
        )


def test_clear_manager():

    manager = StrategyManager()
    strategy = DummyStrategy(
        name="Dummy",
        symbol="NIFTY",
    )

    manager.add(strategy)
    manager.clear()

    assert len(manager) == 0


def test_contains():

    manager = StrategyManager()
    strategy = DummyStrategy(
        name="Dummy",
        symbol="NIFTY",
    )

    manager.add(strategy)

    assert "Dummy" in manager
    assert "Missing" not in manager