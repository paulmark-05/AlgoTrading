from datetime import timedelta
from decimal import Decimal

from reporting.html_reporter import HTMLReporter


def test_html_reporter_name():

    reporter = HTMLReporter()

    assert reporter.name == "HTMLReporter"


def test_html_reporter_saves_file(tmp_path):

    reporter = HTMLReporter()

    report = {
        "total_return": Decimal("0.10"),
        "max_drawdown": Decimal("5000"),
        "average_duration": timedelta(minutes=10),
    }

    path = reporter.save(
        report=report,
        path=tmp_path / "report.html",
    )

    assert path.exists()

    text = path.read_text(
        encoding="utf-8",
    )

    assert "<h1>Backtest Report</h1>" in text
    assert "total_return" in text
    assert "0.10" in text
    assert "average_duration" in text
    assert "0:10:00" in text