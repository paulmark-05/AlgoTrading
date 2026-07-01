from __future__ import annotations

from decimal import Decimal

from analytics.cagr import CAGRCalculator
from analytics.drawdown import DrawdownCalculator
from analytics.performance_tracker import PerformanceTracker


class CalmarCalculator:

    def __init__(
        self,
        tracker: PerformanceTracker,
        periods_per_year: int = 252,
    ) -> None:

        self.tracker = tracker
        self.periods_per_year = periods_per_year

    def calculate(self) -> Decimal:

        max_drawdown = DrawdownCalculator(
            self.tracker
        ).max_drawdown()

        if max_drawdown == 0:
            return Decimal("0")

        snapshots = self.tracker.all()

        if not snapshots:
            return Decimal("0")

        starting_equity = snapshots[0].total_value

        if starting_equity == 0:
            return Decimal("0")

        drawdown_pct = max_drawdown / starting_equity

        if drawdown_pct == 0:
            return Decimal("0")

        cagr = CAGRCalculator(
            self.tracker,
            periods_per_year=self.periods_per_year,
        ).calculate()

        return cagr / drawdown_pct