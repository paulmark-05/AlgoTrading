import pandas as pd
import pytest

from strategy.context import StrategyContext


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


def test_context_creation():
    context = StrategyContext(
        symbol="nifty",
        data=sample_df(),
    )

    assert context.symbol == "NIFTY"


def test_latest_row():
    context = StrategyContext(
        symbol="NIFTY",
        data=sample_df(),
    )

    assert context.latest["close"] == 105


def test_empty_symbol_rejected():
    with pytest.raises(ValueError):
        StrategyContext(
            symbol="",
            data=sample_df(),
        )


def test_empty_data_rejected():
    with pytest.raises(ValueError):
        StrategyContext(
            symbol="NIFTY",
            data=pd.DataFrame(),
        )


def test_context_is_immutable():
    context = StrategyContext(
        symbol="NIFTY",
        data=sample_df(),
    )

    with pytest.raises(Exception):
        context.symbol = "BANKNIFTY"