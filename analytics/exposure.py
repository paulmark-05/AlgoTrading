from __future__ import annotations

from decimal import Decimal

from analytics.performance_tracker import PerformanceTracker


class ExposureCalculator:

    def __init__(
        self,
        tracker: PerformanceTracker,
    ) -> None:
        self.tracker = tracker

    def exposure_ratio(self) -> Decimal:

        snapshots = self.tracker.all()

        if not snapshots:
            return Decimal("0")

        exposed = [
            snapshot
            for snapshot in snapshots
            if snapshot.market_value > 0
        ]

        return (
            Decimal(len(exposed))
            / Decimal(len(snapshots))
        )