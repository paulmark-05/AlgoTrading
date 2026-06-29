import pandas as pd

from indicators.base_indicator import BaseIndicator


class DummyIndicator(BaseIndicator):

    @property
    def name(self):
        return "Dummy"

    def calculate(self, data):
        return data["close"]


def test_indicator_name():

    indicator = DummyIndicator()

    assert indicator.name == "Dummy"


def test_indicator_calculate():

    indicator = DummyIndicator()

    df = pd.DataFrame(
        {
            "close": [100, 101, 102]
        }
    )

    result = indicator.calculate(df)

    assert len(result) == 3
    assert result.iloc[-1] == 102