from datetime import timedelta
from decimal import Decimal

from openpyxl import load_workbook

from reporting.excel_reporter import ExcelReporter


def test_excel_reporter_name():

    reporter = ExcelReporter()

    assert reporter.name == "ExcelReporter"


def test_excel_reporter_saves_file(tmp_path):

    reporter = ExcelReporter()

    report = {
        "total_return": Decimal("0.10"),
        "max_drawdown": Decimal("5000"),
        "average_duration": timedelta(minutes=10),
    }

    path = reporter.save(
        report=report,
        path=tmp_path / "report.xlsx",
    )

    assert path.exists()

    workbook = load_workbook(path)
    sheet = workbook["Report"]

    assert sheet["A1"].value == "Metric"
    assert sheet["B1"].value == "Value"

    assert sheet["A2"].value == "total_return"
    assert sheet["B2"].value == "0.10"
    