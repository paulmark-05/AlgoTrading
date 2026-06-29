from decimal import Decimal

from analytics.performance_snapshot import PerformanceSnapshot
from analytics.performance_tracker import PerformanceTracker


def make_snapshot(index: int):

    return PerformanceSnapshot(
        timestamp=f"2025-01-0{index}",
        cash=Decimal("100000"),
        market_value=Decimal(str(index * 100)),
        total_value=Decimal(str(100000 + index * 100)),
        realized_pnl=Decimal("0"),
        unrealized_pnl=Decimal(str(index * 100)),
        total_pnl=Decimal(str(index * 100)),
    )


def test_new_tracker():

    tracker = PerformanceTracker()

    assert len(tracker) == 0
    assert tracker.latest() is None


def test_add_snapshot():

    tracker = PerformanceTracker()

    snap = make_snapshot(1)

    tracker.add(snap)

    assert len(tracker) == 1
    assert tracker.latest() is snap


def test_multiple_snapshots():

    tracker = PerformanceTracker()

    s1 = make_snapshot(1)
    s2 = make_snapshot(2)
    s3 = make_snapshot(3)

    tracker.add(s1)
    tracker.add(s2)
    tracker.add(s3)

    assert len(tracker) == 3
    assert tracker.latest() is s3


def test_all_returns_copy():

    tracker = PerformanceTracker()

    tracker.add(make_snapshot(1))

    snapshots = tracker.all()

    snapshots.clear()

    assert len(tracker) == 1


def test_clear():

    tracker = PerformanceTracker()

    tracker.add(make_snapshot(1))
    tracker.add(make_snapshot(2))

    tracker.clear()

    assert len(tracker) == 0
    assert tracker.latest() is None