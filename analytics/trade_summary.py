from __future__ import annotations

from decimal import Decimal

from analytics.trade_ledger import ClosedTrade


class TradeSummary:

    def __init__(
        self,
        closed_trades: list[ClosedTrade],
    ) -> None:
        self.closed_trades = closed_trades

    def count(self) -> int:
        return len(self.closed_trades)

    def winners(self) -> list[ClosedTrade]:
        return [
            trade
            for trade in self.closed_trades
            if trade.is_winner
        ]

    def losers(self) -> list[ClosedTrade]:
        return [
            trade
            for trade in self.closed_trades
            if trade.is_loser
        ]

    def win_rate(self) -> Decimal:

        if not self.closed_trades:
            return Decimal("0")

        return (
            Decimal(len(self.winners()))
            / Decimal(len(self.closed_trades))
        )

    def gross_profit(self) -> Decimal:

        return sum(
            (
                trade.net_pnl
                for trade in self.winners()
            ),
            start=Decimal("0"),
        )

    def gross_loss(self) -> Decimal:

        return sum(
            (
                trade.net_pnl
                for trade in self.losers()
            ),
            start=Decimal("0"),
        )

    def net_pnl(self) -> Decimal:

        return sum(
            (
                trade.net_pnl
                for trade in self.closed_trades
            ),
            start=Decimal("0"),
        )

    def profit_factor(self) -> Decimal:

        gross_loss = abs(
            self.gross_loss()
        )

        if gross_loss == 0:
            return Decimal("0")

        return self.gross_profit() / gross_loss

    def average_win(self) -> Decimal:

        winners = self.winners()

        if not winners:
            return Decimal("0")

        return self.gross_profit() / Decimal(len(winners))


    def average_loss(self) -> Decimal:

        losers = self.losers()

        if not losers:
            return Decimal("0")

        return abs(
            self.gross_loss()
        ) / Decimal(len(losers))


    def largest_win(self) -> Decimal:

        winners = self.winners()

        if not winners:
            return Decimal("0")

        return max(
            trade.net_pnl
            for trade in winners
        )


    def largest_loss(self) -> Decimal:

        losers = self.losers()

        if not losers:
            return Decimal("0")

        return min(
            trade.net_pnl
            for trade in losers
        )


    def average_trade(self) -> Decimal:

        if self.count() == 0:
            return Decimal("0")

        return (
            self.net_pnl()
            / Decimal(self.count())
        )