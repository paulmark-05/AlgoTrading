from datetime import timedelta
from decimal import Decimal

from reporting.markdown_reporter import MarkdownReporter


def test_markdown_reporter_name():

    reporter = MarkdownReporter()

    assert reporter.name == "MarkdownReporter"


def test_markdown_reporter_saves_file(tmp_path):

    reporter = MarkdownReporter()

    report = {
        "total_return": Decimal("0.10"),
        "max_drawdown": Decimal("5000"),
        "average_duration": timedelta(minutes=10),
    }

    path = reporter.save(
        report=report,
        path=tmp_path / "report.md",
    )

    assert path.exists()

    text = path.read_text(
        encoding="utf-8",
    )

    assert "# Backtest Report" in text
    assert "| Metric | Value |" in text
    assert "| total_return | 0.10 |" in text
    assert "| average_duration | 0:10:00 |" in text