from decimal import Decimal

from reporting.csv_reporter import CSVReporter
from reporting.html_reporter import HTMLReporter
from reporting.json_reporter import JSONReporter
from reporting.report_manager import ReportManager


def test_report_manager_add_get():

    manager = ReportManager()
    reporter = JSONReporter()

    manager.add(reporter)

    assert len(manager) == 1
    assert manager.get("JSONReporter") is reporter


def test_report_manager_export_all(tmp_path):

    manager = ReportManager()

    manager.add(JSONReporter())
    manager.add(CSVReporter())
    manager.add(HTMLReporter())

    report = {
        "total_return": Decimal("0.10"),
    }

    paths = manager.export_all(
        report=report,
        output_dir=tmp_path,
    )

    assert len(paths) == 3
    assert (tmp_path / "report.json").exists()
    assert (tmp_path / "report.csv").exists()
    assert (tmp_path / "report.html").exists()


def test_report_manager_clear():

    manager = ReportManager()

    manager.add(JSONReporter())
    manager.clear()

    assert len(manager) == 0
    