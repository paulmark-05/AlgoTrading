import json
from decimal import Decimal
from datetime import timedelta

from reporting.json_reporter import JSONReporter


def test_json_reporter_saves_file(tmp_path):

    reporter = JSONReporter()

    report = {
        "total_return": Decimal("0.10"),
        "max_drawdown": Decimal("5000"),
        "average_duration": timedelta(minutes=10),
    }

    path = reporter.save(
        report=report,
        path=tmp_path / "report.json",
    )

    assert path.exists()

    data = json.loads(
        path.read_text(
            encoding="utf-8"
        )
    )
def test_json_reporter_name():

    reporter = JSONReporter()

    assert reporter.name == "JSONReporter"
    