from __future__ import annotations

from pathlib import Path

from reporting.base_reporter import BaseReporter


class ReportManager:

    def __init__(self) -> None:
        self._reporters: dict[str, BaseReporter] = {}

    def add(
        self,
        reporter: BaseReporter,
    ) -> None:
        self._reporters[reporter.name] = reporter

    def get(
        self,
        name: str,
    ) -> BaseReporter | None:
        return self._reporters.get(name)

    def export_all(
        self,
        *,
        report: dict,
        output_dir: str | Path,
    ) -> list[Path]:

        output_dir = Path(output_dir)
        paths = []

        for reporter in self._reporters.values():

            extension_map = {
                "JSONReporter": "json",
                "CSVReporter": "csv",
                "HTMLReporter": "html",
                "MarkdownReporter": "md",
                "ExcelReporter": "xlsx",
            }

            extension = extension_map.get(
                reporter.name,
                reporter.name.replace("Reporter", "").lower(),
            )

            path = output_dir / f"report.{extension}"

            paths.append(
                reporter.save(
                    report=report,
                    path=path,
                )
            )

        return paths

    def clear(self) -> None:
        self._reporters.clear()

    def __len__(self) -> int:
        return len(self._reporters)