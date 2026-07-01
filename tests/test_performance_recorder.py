from decimal import Decimal

from analytics.performance_tracker import PerformanceTracker
from broker.paper_broker import PaperBroker
from engine.performance_recorder import PerformanceRecorder


def test_performance_recorder_records_snapshot():

    tracker = PerformanceTracker()

    recorder = PerformanceRecorder(
        tracker=tracker,
    )

    broker = PaperBroker(
        initial_cash=Decimal("100000")
    )

    snapshot = recorder.record(
        timestamp="2025-01-01",
        broker=broker,
    )

    assert len(tracker) == 1
    assert tracker.latest() is snapshot
    assert snapshot.cash == Decimal("100000")
    assert snapshot.total_value == Decimal("100000")


def test_performance_recorder_after_position_update():

    tracker = PerformanceTracker()
    recorder = PerformanceRecorder(tracker)

    broker = PaperBroker(
        initial_cash=Decimal("100000")
    )

    broker.update_market_price(
        "NIFTY",
        Decimal("100"),
    )

    snapshot = recorder.record(
        timestamp="2025-01-01",
        broker=broker,
    )

    assert snapshot.market_value == Decimal("0")
    assert snapshot.total_pnl == Decimal("0")