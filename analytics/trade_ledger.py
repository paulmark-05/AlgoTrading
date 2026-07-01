from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal

from broker.enums import OrderSide
from broker.trade import Trade
from broker.trade_book import TradeBook
from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal

@dataclass(frozen=True, slots=True)
class ClosedTrade:
    symbol: str
    quantity: int
    entry_price: Decimal
    exit_price: Decimal
    gross_pnl: Decimal
    commission: Decimal
    net_pnl: Decimal

    entry_time: datetime | None = None
    exit_time: datetime | None = None

    @property
    def is_winner(self) -> bool:
        return self.net_pnl > 0

    @property
    def is_loser(self) -> bool:
        return self.net_pnl < 0


class TradeLedger:

    def __init__(
        self,
        trade_book: TradeBook,
    ) -> None:
        self.trade_book = trade_book

    def closed_trades(self) -> list[ClosedTrade]:

        closed: list[ClosedTrade] = []

        open_qty = 0
        avg_entry = Decimal("0")
        entry_commission = Decimal("0")

        for trade in self.trade_book:

            if trade.side == OrderSide.BUY:

                existing_cost = avg_entry * open_qty

                new_cost = (
                    trade.price
                    * Decimal(trade.quantity)
                )

                open_qty += trade.quantity

                avg_entry = (
                    existing_cost + new_cost
                ) / Decimal(open_qty)

                entry_commission += trade.commission

            elif trade.side == OrderSide.SELL:

                if open_qty <= 0:
                    continue

                close_qty = min(
                    trade.quantity,
                    open_qty,
                )

                gross_pnl = (
                    trade.price - avg_entry
                ) * Decimal(close_qty)

                allocated_entry_commission = (
                    entry_commission
                    * Decimal(close_qty)
                    / Decimal(open_qty)
                )

                allocated_exit_commission = (
                    trade.commission
                    * Decimal(close_qty)
                    / Decimal(trade.quantity)
                )

                commission = (
                    allocated_entry_commission
                    + allocated_exit_commission
                )

                net_pnl = gross_pnl - commission

                closed.append(
                    ClosedTrade(
                        symbol=trade.symbol,
                        quantity=close_qty,
                        entry_price=avg_entry,
                        exit_price=trade.price,
                        gross_pnl=gross_pnl,
                        commission=commission,
                        net_pnl=net_pnl,
                    )
                )

                open_qty -= close_qty
                entry_commission -= allocated_entry_commission

                if open_qty == 0:
                    avg_entry = Decimal("0")
                    entry_commission = Decimal("0")

        return closed