from decimal import Decimal

from analytics.performance_snapshot import PerformanceSnapshot
from analytics.performance_tracker import PerformanceTracker
from analytics.sortino import SortinoCalculator


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


def test_empty_sortino():

    tracker = PerformanceTracker()

    calc = SortinoCalculator(tracker)

    assert calc.calculate() == Decimal("0")


def test_sortino_positive():

    tracker = PerformanceTracker()

    tracker.add(make_snapshot("100"))
    tracker.add(make_snapshot("110"))
    tracker.add(make_snapshot("100"))
    tracker.add(make_snapshot("120"))
    tracker.add(make_snapshot("115"))

    calc = SortinoCalculator(tracker)

    result = calc.calculate()

    assert isinstance(result, Decimal)