from __future__ import annotations

from datetime import timedelta

from analytics.trade_ledger import ClosedTrade


class TradeDurationCalculator:

    def __init__(
        self,
        trades: list[ClosedTrade],
    ) -> None:

        self.trades = trades

    def average_duration(self) -> timedelta:

        durations = []

        for trade in self.trades:

            if (
                trade.entry_time is None
                or trade.exit_time is None
            ):
                continue

            durations.append(
                trade.exit_time - trade.entry_time
            )

        if not durations:
            return timedelta()

        total = sum(
            durations,
            timedelta(),
        )

        return total / len(durations)

    def longest_duration(self) -> timedelta:

        durations = [
            trade.exit_time - trade.entry_time
            for trade in self.trades
            if trade.entry_time is not None
            and trade.exit_time is not None
        ]

        if not durations:
            return timedelta()

        return max(durations)

    def shortest_duration(self) -> timedelta:

        durations = [
            trade.exit_time - trade.entry_time
            for trade in self.trades
            if trade.entry_time is not None
            and trade.exit_time is not None
        ]

        if not durations:
            return timedelta()

        return min(durations)