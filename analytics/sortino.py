from __future__ import annotations

from decimal import Decimal
import math

from analytics.performance_tracker import PerformanceTracker
from analytics.returns import ReturnsCalculator
from analytics.statistics import Statistics


class SortinoCalculator:
    """
    Calculates the Sortino Ratio.
    """

    def __init__(
        self,
        tracker: PerformanceTracker,
        risk_free_rate: Decimal = Decimal("0"),
    ) -> None:

        self.tracker = tracker
        self.risk_free_rate = Decimal(risk_free_rate)

    def calculate(self) -> Decimal:

        returns = ReturnsCalculator(
            self.tracker
        ).returns_series()

        if not returns:
            return Decimal("0")

        excess_returns = [
            r - self.risk_free_rate
            for r in returns
        ]

        mean_return = Statistics.mean(excess_returns)

        downside = [
            r
            for r in excess_returns
            if r < 0
        ]

        if not downside:
            return Decimal("0")

        downside_mean = Statistics.mean(downside)

        variance = sum(
            (r - downside_mean) ** 2
            for r in downside
        ) / Decimal(len(downside))

        downside_std = Decimal(
            str(
                math.sqrt(
                    float(variance)
                )
            )
        )

        if downside_std == 0:
            return Decimal("0")

        return mean_return / downside_std