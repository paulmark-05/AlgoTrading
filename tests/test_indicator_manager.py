import pandas as pd

from indicators.ema import EMA
from indicators.manager import IndicatorManager
from indicators.sma import SMA


def sample_df():

    return pd.DataFrame(
        {
            "close": [10, 20, 30, 40, 50]
        }
    )


def test_empty_manager():

    manager = IndicatorManager()

    assert manager.calculate(sample_df()) == {}


def test_single_indicator():

    manager = IndicatorManager()

    manager.add(SMA(3))

    result = manager.calculate(sample_df())

    assert "SMA_3" in result
    assert len(result["SMA_3"]) == 5


def test_multiple_indicators():

    manager = IndicatorManager()

    manager.add(SMA(3))
    manager.add(EMA(3))

    result = manager.calculate(sample_df())

    assert "SMA_3" in result
    assert "EMA_3" in result


def test_clear():

    manager = IndicatorManager()

    manager.add(SMA(3))
    manager.clear()

    assert manager.calculate(sample_df()) == {}