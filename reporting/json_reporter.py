from __future__ import annotations

import json
from decimal import Decimal
from pathlib import Path
from datetime import timedelta
from reporting.base_reporter import BaseReporter

class JSONReporter(BaseReporter):
    
    @property
    def name(self) -> str:

        return "JSONReporter"

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
            encoding="utf-8",
        ) as file:
            json.dump(
                report,
                file,
                indent=4,
                default=self._serialize,
            )

        return path

    def _serialize(
        self,
        value,
    ):

        if isinstance(value, Decimal):
            return str(value)

        if isinstance(value, timedelta):
            return str(value)

        return str(value)