import pandas as pd
import pytest

from strategy.context import StrategyContext
from strategy.reference.noop_strategy import NoOpStrategy
from strategy.signal import SignalSide


def sample_context(symbol="NIFTY"):

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
        symbol=symbol,
        data=data,
    )


def test_noop_strategy_creation():

    strategy = NoOpStrategy(
        symbol="NIFTY"
    )

    assert strategy.name == "NoOpStrategy"
    assert strategy.symbol == "NIFTY"


def test_noop_strategy_returns_hold():

    strategy = NoOpStrategy(
        symbol="NIFTY"
    )

    signal = strategy.generate_signal(
        sample_context()
    )

    assert signal.symbol == "NIFTY"
    assert signal.side == SignalSide.HOLD
    assert signal.is_hold is True


def test_noop_strategy_rejects_wrong_symbol():

    strategy = NoOpStrategy(
        symbol="NIFTY"
    )

    with pytest.raises(ValueError):
        strategy.generate_signal(
            sample_context("BANKNIFTY")
        )