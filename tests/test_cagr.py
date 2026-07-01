from decimal import Decimal

import pytest

from analytics.cagr import CAGRCalculator
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


def test_empty_cagr():

    tracker = PerformanceTracker()

    calc = CAGRCalculator(
        tracker,
        periods_per_year=252,
    )

    assert calc.calculate() == Decimal("0")


def test_invalid_periods_per_year():

    tracker = PerformanceTracker()

    with pytest.raises(ValueError):
        CAGRCalculator(
            tracker,
            periods_per_year=0,
        )


def test_cagr_positive():

    tracker = PerformanceTracker()

    tracker.add(make_snapshot("100"))
    tracker.add(make_snapshot("110"))
    tracker.add(make_snapshot("121"))

    calc = CAGRCalculator(
        tracker,
        periods_per_year=2,
    )

    assert calc.calculate() == pytest.approx(
        Decimal("0.21")
    )
    