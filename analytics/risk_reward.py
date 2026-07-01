from __future__ import annotations

from decimal import Decimal

from analytics.trade_summary import TradeSummary


class RiskRewardCalculator:

    def __init__(
        self,
        summary: TradeSummary,
    ) -> None:
        self.summary = summary

    def calculate(self) -> Decimal:

        average_loss = self.summary.average_loss()

        if average_loss == 0:
            return Decimal("0")

        return self.summary.average_win() / average_loss