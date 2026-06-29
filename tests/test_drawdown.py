from decimal import Decimal

from analytics.drawdown import DrawdownCalculator
from analytics.performance_snapshot import PerformanceSnapshot
from analytics.performance_tracker import PerformanceTracker


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


def test_empty_tracker():

    tracker = PerformanceTracker()

    dd = DrawdownCalculator(tracker)

    assert dd.max_drawdown() == Decimal("0")


def test_no_drawdown():

    tracker = PerformanceTracker()

    tracker.add(make_snapshot("100"))
    tracker.add(make_snapshot("110"))
    tracker.add(make_snapshot("120"))

    dd = DrawdownCalculator(tracker)

    assert dd.series() == [
        Decimal("0"),
        Decimal("0"),
        Decimal("0"),
    ]

    assert dd.max_drawdown() == Decimal("0")


def test_drawdown():

    tracker = PerformanceTracker()

    tracker.add(make_snapshot("100"))
    tracker.add(make_snapshot("120"))
    tracker.add(make_snapshot("115"))
    tracker.add(make_snapshot("105"))
    tracker.add(make_snapshot("130"))

    dd = DrawdownCalculator(tracker)

    assert dd.series() == [
        Decimal("0"),
        Decimal("0"),
        Decimal("5"),
        Decimal("15"),
        Decimal("0"),
    ]

    assert dd.max_drawdown() == Decimal("15")