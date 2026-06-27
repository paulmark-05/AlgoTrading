"""
portfolio.py

Portfolio accounting.

The Portfolio owns:

- Cash balance
- Open positions
- Portfolio valuation
- Applying executed trades

Position-specific accounting is delegated to Position.
"""

from __future__ import annotations

from decimal import Decimal

from broker.position import Position
from broker.trade import Trade


class Portfolio:
    """
    Represents the trading account portfolio.
    """

    def __init__(
        self,
        initial_cash: Decimal | float | int,
    ) -> None:

        self._cash = Decimal(initial_cash)

        if self._cash < 0:
            raise ValueError(
                "Initial cash cannot be negative."
            )

        self._positions: dict[str, Position] = {}

    # ---------------------------------------------------------
    # Trade Processing
    # ---------------------------------------------------------

    def apply_trade(
        self,
        trade: Trade,
    ) -> None:
        """
        Apply an executed trade to the portfolio.
        """

        position = self._positions.get(trade.symbol)

        if position is None:
            position = Position(trade.symbol)
            self._positions[trade.symbol] = position

        position.apply_trade(trade)

        if trade.is_buy:
            self._cash -= trade.net_value
        else:
            self._cash += trade.net_value

        if position.quantity == 0:
            del self._positions[trade.symbol]

    # ---------------------------------------------------------
    # Market Prices
    # ---------------------------------------------------------

    def update_market_price(
        self,
        symbol: str,
        price: Decimal | float | int,
    ) -> None:

        symbol = symbol.upper()

        position = self._positions.get(symbol)

        if position is not None:
            position.update_market_price(
                Decimal(price)
            )

    # ---------------------------------------------------------
    # Position Access
    # ---------------------------------------------------------

    def has_position(
        self,
        symbol: str,
    ) -> bool:

        return symbol.upper() in self._positions

    def get_position(
        self,
        symbol: str,
    ) -> Position | None:

        return self._positions.get(
            symbol.upper()
        )

    @property
    def positions(self) -> dict[str, Position]:
        """
        Read-only view of positions.
        """

        return dict(self._positions)

    # ---------------------------------------------------------
    # Cash
    # ---------------------------------------------------------

    @property
    def cash(self) -> Decimal:
        return self._cash

    # ---------------------------------------------------------
    # Portfolio Metrics
    # ---------------------------------------------------------

    @property
    def market_value(self) -> Decimal:

        return sum(
            (
                position.market_value
                for position in self._positions.values()
            ),
            start=Decimal("0"),
        )

    @property
    def total_value(self) -> Decimal:

        return self.cash + self.market_value

    @property
    def total_cost_basis(self) -> Decimal:

        return sum(
            (
                position.cost_basis
                for position in self._positions.values()
            ),
            start=Decimal("0"),
        )

    @property
    def unrealized_pnl(self) -> Decimal:

        return sum(
            (
                position.unrealized_pnl
                for position in self._positions.values()
            ),
            start=Decimal("0"),
        )

    @property
    def realized_pnl(self) -> Decimal:

        return sum(
            (
                position.realized_pnl
                for position in self._positions.values()
            ),
            start=Decimal("0"),
        )

    @property
    def total_pnl(self) -> Decimal:

        return (
            self.realized_pnl
            + self.unrealized_pnl
        )

    # ---------------------------------------------------------
    # Utility
    # ---------------------------------------------------------

    def reset(self) -> None:

        self._positions.clear()

    def __len__(self) -> int:

        return len(self._positions)

    def __contains__(
        self,
        symbol: str,
    ) -> bool:

        return symbol.upper() in self._positions

    def __repr__(self) -> str:

        return (
            "Portfolio("
            f"cash={self.cash}, "
            f"market_value={self.market_value}, "
            f"total_value={self.total_value}, "
            f"positions={len(self._positions)})"
        )