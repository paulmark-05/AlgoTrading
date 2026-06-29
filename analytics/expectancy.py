from __future__ import annotations

from decimal import Decimal

from analytics.trade_summary import TradeSummary


class ExpectancyCalculator:
    """
    Calculates the average expected profit
    per completed trade.
    """

    def __init__(
        self,
        summary: TradeSummary,
    ) -> None:

        self.summary = summary

    def calculate(self) -> Decimal:

        if self.summary.count() == 0:
            return Decimal("0")

        return (
            self.summary.net_pnl()
            / Decimal(self.summary.count())
        )