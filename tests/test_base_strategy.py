

from decimal import Decimal

import pandas as pd
import pytest

from strategy.base_strategy import BaseStrategy
from strategy.signal import Signal, SignalSide


class DummyStrategy(BaseStrategy):

    def generate_signal(
        self,
        data: pd.DataFrame,
    ) -> Signal:

        self.validate_data(data)

        return Signal(
            symbol=self.symbol,
            side=SignalSide.HOLD,
            strength=Decimal("1"),
        )


def sample_df():

    return pd.DataFrame(
        {
            "datetime": ["2025-01-01"],
            "open": [100],
            "high": [101],
            "low": [99],
            "close": [100],
            "volume": [1000],
        }
    )


def test_strategy_creation():

    strategy = DummyStrategy(
        "Dummy",
        "NIFTY",
    )

    assert strategy.name == "Dummy"
    assert strategy.symbol == "NIFTY"


def test_empty_name_rejected():

    with pytest.raises(ValueError):
        DummyStrategy(
            "",
            "NIFTY",
        )


def test_empty_symbol_rejected():

    with pytest.raises(ValueError):
        DummyStrategy(
            "Dummy",
            "",
        )


def test_generate_signal():

    strategy = DummyStrategy(
        "Dummy",
        "NIFTY",
    )

    signal = strategy.generate_signal(
        sample_df()
    )

    assert signal.side == SignalSide.HOLD


def test_empty_dataframe_rejected():

    strategy = DummyStrategy(
        "Dummy",
        "NIFTY",
    )

    with pytest.raises(ValueError):
        strategy.validate_data(
            pd.DataFrame()
        )


def test_missing_columns_rejected():

    strategy = DummyStrategy(
        "Dummy",
        "NIFTY",
    )

    df = pd.DataFrame(
        {
            "close": [100]
        }
    )

    with pytest.raises(ValueError):
        strategy.validate_data(df)


def test_repr():

    strategy = DummyStrategy(
        "Dummy",
        "NIFTY",
    )

    assert "BaseStrategy" in repr(strategy)