from __future__ import annotations

from datetime import timedelta
from decimal import Decimal
from html import escape
from pathlib import Path

from reporting.base_reporter import BaseReporter


class HTMLReporter(BaseReporter):

    @property
    def name(self) -> str:
        return "HTMLReporter"

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

        rows = []

        for key, value in report.items():
            rows.append(
                "<tr>"
                f"<td>{escape(str(key))}</td>"
                f"<td>{escape(self._serialize(value))}</td>"
                "</tr>"
            )

        html = (
            "<!DOCTYPE html>"
            "<html>"
            "<head>"
            "<meta charset='utf-8'>"
            "<title>Backtest Report</title>"
            "</head>"
            "<body>"
            "<h1>Backtest Report</h1>"
            "<table border='1'>"
            "<thead><tr><th>Metric</th><th>Value</th></tr></thead>"
            "<tbody>"
            + "".join(rows)
            + "</tbody></table>"
            "</body>"
            "</html>"
        )

        path.write_text(
            html,
            encoding="utf-8",
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