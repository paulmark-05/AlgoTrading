from __future__ import annotations

from decimal import Decimal

from broker.trade_book import TradeBook


class WinRateCalculator:

    def __init__(
        self,
        trade_book: TradeBook,
    ) -> None:
        self.trade_book = trade_book

    def calculate(self) -> Decimal:
        """
        Placeholder until closed-trade grouping is added.

        Current TradeBook stores individual fills, not completed
        round-trip trades, so win rate cannot be calculated correctly yet.
        """
        return Decimal("0")