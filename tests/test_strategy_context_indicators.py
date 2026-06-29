import pandas as pd

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


def test_context_indicator_lookup():

    context = StrategyContext(
        symbol="NIFTY",
        data=sample_df(),
        indicators={
            "EMA_20": "dummy-ema"
        },
    )

    assert context.indicator("EMA_20") == "dummy-ema"


def test_context_missing_indicator_returns_none():

    context = StrategyContext(
        symbol="NIFTY",
        data=sample_df(),
    )

    assert context.indicator("RSI_14") is None