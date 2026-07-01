from __future__ import annotations

from datetime import timedelta
from decimal import Decimal
from pathlib import Path

from openpyxl import Workbook

from reporting.base_reporter import BaseReporter


class ExcelReporter(BaseReporter):

    @property
    def name(self) -> str:
        return "ExcelReporter"

    def save(
        self,
        *,
        report: dict,
        path: str | Path,
    ) -> Path:

        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)

        workbook = Workbook()
        sheet = workbook.active
        sheet.title = "Report"

        sheet.append(["Metric", "Value"])

        for key, value in report.items():
            sheet.append(
                [
                    str(key),
                    self._serialize(value),
                ]
            )

        workbook.save(path)

        return path

    def _serialize(
        self,
        value,
    ) -> str:

        if isinstance(value, Decimal):
            return str(value)

        if isinstance(value, timedelta):
            return str(value)

        return str(value)