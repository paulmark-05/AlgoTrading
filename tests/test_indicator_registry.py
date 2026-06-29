import pandas as pd

from indicators.base_indicator import BaseIndicator
from indicators.registry import IndicatorRegistry


class DummyIndicator(BaseIndicator):

    @property
    def name(self):
        return "Dummy"

    def calculate(self, data):
        return data["close"]


def test_new_registry():

    registry = IndicatorRegistry()

    assert len(registry) == 0


def test_add_indicator():

    registry = IndicatorRegistry()
    indicator = DummyIndicator()

    registry.add(indicator)

    assert len(registry) == 1
    assert registry.has("Dummy")


def test_get_indicator():

    registry = IndicatorRegistry()
    indicator = DummyIndicator()

    registry.add(indicator)

    assert registry.get("Dummy") is indicator


def test_missing_indicator_returns_none():

    registry = IndicatorRegistry()

    assert registry.get("Missing") is None


def test_all_indicators():

    registry = IndicatorRegistry()
    indicator = DummyIndicator()

    registry.add(indicator)

    assert registry.all() == [indicator]


def test_clear_registry():

    registry = IndicatorRegistry()
    registry.add(DummyIndicator())

    registry.clear()

    assert len(registry) == 0


def test_contains():

    registry = IndicatorRegistry()
    registry.add(DummyIndicator())

    assert "Dummy" in registry
    assert "Missing" not in registry