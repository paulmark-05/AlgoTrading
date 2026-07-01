from decimal import Decimal

from analytics.exposure import ExposureCalculator
from analytics.performance_snapshot import PerformanceSnapshot
from analytics.performance_tracker import PerformanceTracker


def make_snapshot(
    total_value,
    market_value,
):

    return PerformanceSnapshot(
        timestamp=None,
        cash=Decimal(total_value) - Decimal(market_value),
        market_value=Decimal(market_value),
        total_value=Decimal(total_value),
        realized_pnl=Decimal("0"),
        unrealized_pnl=Decimal("0"),
        total_pnl=Decimal("0"),
    )


def test_empty_exposure():

    tracker = PerformanceTracker()

    calc = ExposureCalculator(tracker)

    assert calc.exposure_ratio() == Decimal("0")


def test_zero_exposure():

    tracker = PerformanceTracker()

    tracker.add(make_snapshot("100000", "0"))
    tracker.add(make_snapshot("100000", "0"))

    calc = ExposureCalculator(tracker)

    assert calc.exposure_ratio() == Decimal("0")


def test_partial_exposure():

    tracker = PerformanceTracker()

    tracker.add(make_snapshot("100000", "0"))
    tracker.add(make_snapshot("100000", "50000"))
    tracker.add(make_snapshot("100000", "50000"))
    tracker.add(make_snapshot("100000", "0"))

    calc = ExposureCalculator(tracker)

    assert calc.exposure_ratio() == Decimal("0.5")


def test_full_exposure():

    tracker = PerformanceTracker()

    tracker.add(make_snapshot("100000", "10000"))
    tracker.add(make_snapshot("100000", "20000"))

    calc = ExposureCalculator(tracker)

    assert calc.exposure_ratio() == Decimal("1")