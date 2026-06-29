from decimal import Decimal

from analytics.performance_snapshot import PerformanceSnapshot
from analytics.performance_tracker import PerformanceTracker
from analytics.recovery_factor import RecoveryFactorCalculator


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


def test_empty_recovery_factor():

    tracker = PerformanceTracker()

    calc = RecoveryFactorCalculator(tracker)

    assert calc.calculate() == Decimal("0")


def test_recovery_factor():

    tracker = PerformanceTracker()

    tracker.add(make_snapshot("100"))
    tracker.add(make_snapshot("130"))
    tracker.add(make_snapshot("110"))
    tracker.add(make_snapshot("150"))

    calc = RecoveryFactorCalculator(tracker)

    assert calc.calculate() == Decimal("2.5")