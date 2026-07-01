from decimal import Decimal

from analytics.performance_snapshot import PerformanceSnapshot
from analytics.performance_tracker import PerformanceTracker
from reporting.equity_curve_reporter import EquityCurveReporter


def make_snapshot(value):

    return PerformanceSnapshot(
        timestamp="2025-01-01",
        cash=Decimal(value),
        market_value=Decimal("0"),
        total_value=Decimal(value),
        realized_pnl=Decimal("0"),
        unrealized_pnl=Decimal("0"),
        total_pnl=Decimal("0"),
    )


def test_equity_curve_reporter_saves_file(tmp_path):

    tracker = PerformanceTracker()

    tracker.add(
        make_snapshot("100000")
    )

    reporter = EquityCurveReporter()

    path = reporter.save(
        tracker=tracker,
        path=tmp_path / "equity_curve.csv",
    )

    assert path.exists()

    text = path.read_text(
        encoding="utf-8",
    )

    assert "timestamp,cash,market_value,total_value" in text
    assert "2025-01-01,100000,0,100000" in text