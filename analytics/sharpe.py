from __future__ import annotations

from decimal import Decimal

from analytics.performance_tracker import PerformanceTracker
from analytics.returns import ReturnsCalculator
from analytics.statistics import Statistics


class SharpeCalculator:

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
            value - self.risk_free_rate
            for value in returns
        ]

        mean_return = Statistics.mean(
            excess_returns
        )

        volatility = Statistics.stddev(
            excess_returns
        )

        if volatility == 0:
            return Decimal("0")

        return mean_return / volatility