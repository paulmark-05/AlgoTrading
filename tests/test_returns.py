from decimal import Decimal

from analytics.performance_snapshot import PerformanceSnapshot
from analytics.performance_tracker import PerformanceTracker
from analytics.returns import ReturnsCalculator


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


def test_total_return_empty_tracker():

    tracker = PerformanceTracker()
    calc = ReturnsCalculator(tracker)

    assert calc.total_return() == Decimal("0")


def test_total_return():

    tracker = PerformanceTracker()
    tracker.add(make_snapshot("100"))
    tracker.add(make_snapshot("120"))

    calc = ReturnsCalculator(tracker)

    assert calc.total_return() == Decimal("0.2")


def test_returns_series():

    tracker = PerformanceTracker()
    tracker.add(make_snapshot("100"))
    tracker.add(make_snapshot("110"))
    tracker.add(make_snapshot("121"))

    calc = ReturnsCalculator(tracker)

    assert calc.returns_series() == [
        Decimal("0.1"),
        Decimal("0.1"),
    ]


def test_zero_start_value():

    tracker = PerformanceTracker()
    tracker.add(make_snapshot("0"))
    tracker.add(make_snapshot("100"))

    calc = ReturnsCalculator(tracker)

    assert calc.total_return() == Decimal("0")