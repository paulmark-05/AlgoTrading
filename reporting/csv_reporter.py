from __future__ import annotations

import csv
from datetime import timedelta
from decimal import Decimal
from pathlib import Path
from reporting.base_reporter import BaseReporter

class CSVReporter(BaseReporter):

    @property
    def name(self) -> str:
        return "CSVReporter"

    def save(
        self,
        *,
        report: dict,
        path: str | Path,
    ) -> Path:

        path = Path(path)

        path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with path.open(
            "w",
            newline="",
            encoding="utf-8",
        ) as file:

            writer = csv.writer(file)

            writer.writerow(
                [
                    "Metric",
                    "Value",
                ]
            )

            for key, value in report.items():

                writer.writerow(
                    [
                        key,
                        self._serialize(value),
                    ]
                )

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