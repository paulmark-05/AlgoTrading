from __future__ import annotations

from decimal import Decimal

from analytics.performance_tracker import PerformanceTracker
from analytics.returns import ReturnsCalculator
from analytics.statistics import Statistics


class VolatilityCalculator:

    def __init__(
        self,
        tracker: PerformanceTracker,
    ) -> None:
        self.tracker = tracker

    def calculate(self) -> Decimal:

        returns = ReturnsCalculator(
            self.tracker
        ).returns_series()

        return Statistics.stddev(returns)