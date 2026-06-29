from __future__ import annotations

from decimal import Decimal

from analytics.drawdown import DrawdownCalculator
from analytics.performance_tracker import PerformanceTracker
from analytics.returns import ReturnsCalculator


class PerformanceReport:

    def __init__(
        self,
        tracker: PerformanceTracker,
    ) -> None:
        self.tracker = tracker

    def to_dict(self) -> dict[str, Decimal | int]:

        returns = ReturnsCalculator(
            self.tracker
        )

        drawdown = DrawdownCalculator(
            self.tracker
        )

        return {
            "snapshots": len(self.tracker),
            "total_return": returns.total_return(),
            "max_drawdown": drawdown.max_drawdown(),
        }