from __future__ import annotations

from analytics.trade_summary import TradeSummary


class StreakCalculator:

    def __init__(
        self,
        summary: TradeSummary,
    ) -> None:
        self.summary = summary

    def max_winning_streak(self) -> int:

        best = 0
        current = 0

        for trade in self.summary.closed_trades:

            if trade.is_winner:
                current += 1
                best = max(best, current)
            else:
                current = 0

        return best

    def max_losing_streak(self) -> int:

        best = 0
        current = 0

        for trade in self.summary.closed_trades:

            if trade.is_loser:
                current += 1
                best = max(best, current)
            else:
                current = 0

        return best