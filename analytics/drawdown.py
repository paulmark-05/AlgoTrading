from __future__ import annotations

from decimal import Decimal

from analytics.performance_tracker import PerformanceTracker


class DrawdownCalculator:
    """
    Calculates drawdown statistics from
    PerformanceTracker.
    """

    def __init__(
        self,
        tracker: PerformanceTracker,
    ) -> None:

        self.tracker = tracker

    def series(self) -> list[Decimal]:

        peak = None

        result: list[Decimal] = []

        for snapshot in self.tracker.all():

            equity = snapshot.total_value

            if peak is None or equity > peak:
                peak = equity

            drawdown = peak - equity

            result.append(drawdown)

        return result

    def max_drawdown(self) -> Decimal:

        series = self.series()

        if not series:
            return Decimal("0")

        return max(series)