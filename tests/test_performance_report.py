from decimal import Decimal

from analytics.performance_snapshot import PerformanceSnapshot
from analytics.performance_tracker import PerformanceTracker
from analytics.report import PerformanceReport


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


def test_performance_report():

    tracker = PerformanceTracker()

    tracker.add(make_snapshot("100"))
    tracker.add(make_snapshot("120"))
    tracker.add(make_snapshot("110"))

    report = PerformanceReport(
        tracker
    ).to_dict()

    assert report["snapshots"] == 3
    assert report["total_return"] == Decimal("0.1")
    assert report["max_drawdown"] == Decimal("10")