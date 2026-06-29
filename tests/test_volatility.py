from decimal import Decimal

from analytics.performance_snapshot import PerformanceSnapshot
from analytics.performance_tracker import PerformanceTracker
from analytics.volatility import VolatilityCalculator


def make_snapshot(value):

    return PerformanceSnapshot(
        timestamp=None,
        cash=Decimal(value),
        market_value=Decimal("0"),
        total_value=Decimal(value),
        realized_pnl=Decimal("0"),
        unrealized_pnl=Decimal("0"),
        total_pnl=Decimal("0"),
    )


def test_empty_volatility():

    tracker = PerformanceTracker()

    calc = VolatilityCalculator(tracker)

    assert calc.calculate() == Decimal("0")


def test_volatility_positive():

    tracker = PerformanceTracker()

    tracker.add(make_snapshot("100"))
    tracker.add(make_snapshot("110"))
    tracker.add(make_snapshot("105"))
    tracker.add(make_snapshot("120"))

    calc = VolatilityCalculator(tracker)

    assert calc.calculate() > Decimal("0")