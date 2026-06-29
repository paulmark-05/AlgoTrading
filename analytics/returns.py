from __future__ import annotations

from decimal import Decimal

from analytics.performance_tracker import PerformanceTracker


class ReturnsCalculator:

    def __init__(
        self,
        tracker: PerformanceTracker,
    ) -> None:
        self.tracker = tracker

    def total_return(self) -> Decimal:

        snapshots = self.tracker.all()

        if len(snapshots) < 2:
            return Decimal("0")

        start = snapshots[0].total_value
        end = snapshots[-1].total_value

        if start == 0:
            return Decimal("0")

        return (end - start) / start

    def returns_series(self) -> list[Decimal]:

        snapshots = self.tracker.all()

        if len(snapshots) < 2:
            return []

        result: list[Decimal] = []

        for previous, current in zip(
            snapshots,
            snapshots[1:],
        ):
            if previous.total_value == 0:
                result.append(Decimal("0"))
            else:
                result.append(
                    (
                        current.total_value
                        - previous.total_value
                    )
                    / previous.total_value
                )

        return result