from __future__ import annotations

from decimal import Decimal

from analytics.performance_tracker import PerformanceTracker


class CAGRCalculator:

    def __init__(
        self,
        tracker: PerformanceTracker,
        periods_per_year: int = 252,
    ) -> None:

        if periods_per_year <= 0:
            raise ValueError(
                "Periods per year must be positive."
            )

        self.tracker = tracker
        self.periods_per_year = periods_per_year

    def calculate(self) -> Decimal:

        snapshots = self.tracker.all()

        if len(snapshots) < 2:
            return Decimal("0")

        start = snapshots[0].total_value
        end = snapshots[-1].total_value

        if start <= 0:
            return Decimal("0")

        periods = len(snapshots) - 1
        years = Decimal(periods) / Decimal(self.periods_per_year)

        if years <= 0:
            return Decimal("0")

        result = (
            float(end / start)
            ** float(Decimal("1") / years)
        ) - 1

        return Decimal(str(result))