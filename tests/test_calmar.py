from decimal import Decimal

from analytics.calmar import CalmarCalculator
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


def test_empty_calmar():

    tracker = PerformanceTracker()

    calc = CalmarCalculator(
        tracker,
        periods_per_year=252,
    )

    assert calc.calculate() == Decimal("0")


def test_calmar_zero_drawdown():

    tracker = PerformanceTracker()

    tracker.add(make_snapshot("100"))
    tracker.add(make_snapshot("110"))
    tracker.add(make_snapshot("120"))

    calc = CalmarCalculator(
        tracker,
        periods_per_year=252,
    )

    assert calc.calculate() == Decimal("0")


def test_calmar_positive():

    tracker = PerformanceTracker()

    tracker.add(make_snapshot("100"))
    tracker.add(make_snapshot("130"))
    tracker.add(make_snapshot("110"))
    tracker.add(make_snapshot("150"))

    calc = CalmarCalculator(
        tracker,
        periods_per_year=3,
    )

    assert calc.calculate() > Decimal("0")