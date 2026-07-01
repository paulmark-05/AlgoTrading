from __future__ import annotations

from datetime import timedelta
from decimal import Decimal
from pathlib import Path

from reporting.base_reporter import BaseReporter


class MarkdownReporter(BaseReporter):

    @property
    def name(self) -> str:
        return "MarkdownReporter"

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

        lines = [
            "# Backtest Report",
            "",
            "| Metric | Value |",
            "|---|---|",
        ]

        for key, value in report.items():
            lines.append(
                f"| {key} | {self._serialize(value)} |"
            )

        path.write_text(
            "\n".join(lines),
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