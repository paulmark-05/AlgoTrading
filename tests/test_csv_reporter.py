from datetime import timedelta
from decimal import Decimal

from reporting.csv_reporter import CSVReporter


def test_csv_reporter_saves_file(tmp_path):

    reporter = CSVReporter()

    report = {
        "total_return": Decimal("0.10"),
        "max_drawdown": Decimal("5000"),
        "average_duration": timedelta(minutes=10),
    }

    path = reporter.save(
        report=report,
        path=tmp_path / "report.csv",
    )

    assert path.exists()

    text = path.read_text(
        encoding="utf-8"
    )

def test_csv_reporter_name():
    reporter = CSVReporter()

    assert reporter.name == "CSVReporter"
