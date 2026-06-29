from __future__ import annotations

from decimal import Decimal

from analytics.drawdown import DrawdownCalculator
from analytics.performance_tracker import PerformanceTracker
from analytics.returns import ReturnsCalculator


class RecoveryFactorCalculator:

    def __init__(
        self,
        tracker: PerformanceTracker,
    ) -> None:
        self.tracker = tracker

    def calculate(self) -> Decimal:

        drawdown = DrawdownCalculator(
            self.tracker
        ).max_drawdown()

        if drawdown == 0:
            return Decimal("0")

        snapshots = self.tracker.all()

        if len(snapshots) < 2:
            return Decimal("0")

        net_profit = (
            snapshots[-1].total_value
            - snapshots[0].total_value
        )

        return net_profit / drawdown