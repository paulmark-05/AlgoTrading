from __future__ import annotations

import csv
from pathlib import Path

from analytics.performance_tracker import PerformanceTracker


class EquityCurveReporter:

    def save(
        self,
        *,
        tracker: PerformanceTracker,
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
                    "timestamp",
                    "cash",
                    "market_value",
                    "total_value",
                    "realized_pnl",
                    "unrealized_pnl",
                    "total_pnl",
                ]
            )

            for snapshot in tracker.all():

                writer.writerow(
                    [
                        snapshot.timestamp,
                        snapshot.cash,
                        snapshot.market_value,
                        snapshot.total_value,
                        snapshot.realized_pnl,
                        snapshot.unrealized_pnl,
                        snapshot.total_pnl,
                    ]
                )

        return path