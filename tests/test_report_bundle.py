from decimal import Decimal

from analytics.performance_snapshot import PerformanceSnapshot
from analytics.performance_tracker import PerformanceTracker
from analytics.trade_ledger import ClosedTrade
from config.trading_config import TradingConfig
from reporting.csv_reporter import CSVReporter
from reporting.html_reporter import HTMLReporter
from reporting.json_reporter import JSONReporter
from reporting.markdown_reporter import MarkdownReporter
from reporting.report_bundle import ReportBundle
from reporting.report_manager import ReportManager


def snapshot():

    return PerformanceSnapshot(
        timestamp="2025-01-01",
        cash=Decimal("100000"),
        market_value=Decimal("0"),
        total_value=Decimal("100000"),
        realized_pnl=Decimal("0"),
        unrealized_pnl=Decimal("0"),
        total_pnl=Decimal("0"),
    )


def trade():

    return ClosedTrade(
        symbol="NIFTY",
        quantity=10,
        entry_price=Decimal("100"),
        exit_price=Decimal("110"),
        gross_pnl=Decimal("100"),
        commission=Decimal("0"),
        net_pnl=Decimal("100"),
    )


def test_report_bundle_exports_everything(tmp_path):

    manager = ReportManager()

    manager.add(JSONReporter())
    manager.add(CSVReporter())
    manager.add(HTMLReporter())
    manager.add(MarkdownReporter())

    bundle = ReportBundle(manager)

    tracker = PerformanceTracker()
    tracker.add(snapshot())

    config = TradingConfig(
        symbol="NIFTY",
        initial_cash=Decimal("100000"),
        quantity=10,
        max_drawdown=Decimal("5000"),
    )

    report = {
        "total_return": Decimal("0.15"),
    }

    paths = bundle.export(
        report=report,
        tracker=tracker,
        trades=[trade()],
        config=config,
        output_directory=tmp_path,
    )

    assert len(paths) == 7

    assert (tmp_path / "report.json").exists()
    assert (tmp_path / "report.csv").exists()
    assert (tmp_path / "report.html").exists()
    assert (tmp_path / "report.md").exists()

    assert (tmp_path / "equity_curve.csv").exists()
    assert (tmp_path / "trades.csv").exists()
    assert (tmp_path / "config.json").exists()