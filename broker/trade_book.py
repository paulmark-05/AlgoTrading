from __future__ import annotations

from typing import Dict, Iterator, List, ItemsView, ValuesView

from broker.exceptions import (
    DuplicateTradeError,
    TradeNotFoundError,
)
from broker.trade import Trade


class TradeBook:
    """
    In-memory repository of all executed trades.
    """

    def __init__(self) -> None:

        self._trades: Dict[str, Trade] = {}

    # ---------------------------------------------------------
    # CRUD
    # ---------------------------------------------------------

    def add(self, trade: Trade) -> None:
        """
        Add a trade to the trade book.

        Raises
        ------
        DuplicateTradeError
            If a trade with the same ID already exists.
        """

        if trade.trade_id in self._trades:
            raise DuplicateTradeError(
                f"Trade '{trade.trade_id}' already exists."
            )

        self._trades[trade.trade_id] = trade

    def get(self, trade_id: str) -> Trade:
        """
        Retrieve a trade by ID.
        """

        try:
            return self._trades[trade_id]

        except KeyError as exc:
            raise TradeNotFoundError(
                f"Trade '{trade_id}' not found."
            ) from exc

    def remove(self, trade_id: str) -> Trade:
        """
        Remove a trade from the trade book.
        """

        try:
            return self._trades.pop(trade_id)

        except KeyError as exc:
            raise TradeNotFoundError(
                f"Trade '{trade_id}' not found."
            ) from exc

    def clear(self) -> None:
        """
        Remove all trades.
        """

        self._trades.clear()

    # ---------------------------------------------------------
    # Queries
    # ---------------------------------------------------------

    def has_trade(self, trade_id: str) -> bool:

        return trade_id in self._trades

    def all_trades(self) -> List[Trade]:

        return list(self._trades.values())

    def trades_for_symbol(self, symbol: str) -> List[Trade]:

        return [
            trade
            for trade in self._trades.values()
            if trade.symbol == symbol
        ]

    def values(self) -> ValuesView[Trade]:

        return self._trades.values()

    def items(self) -> ItemsView[str, Trade]:

        return self._trades.items()

    # ---------------------------------------------------------
    # Container Protocol
    # ---------------------------------------------------------

    def __contains__(self, trade_id: str) -> bool:

        return trade_id in self._trades

    def __len__(self) -> int:

        return len(self._trades)

    def __iter__(self) -> Iterator[Trade]:

        return iter(self._trades.values())

    # ---------------------------------------------------------
    # Representation
    # ---------------------------------------------------------

    def __repr__(self) -> str:

        return f"TradeBook(size={len(self)})"