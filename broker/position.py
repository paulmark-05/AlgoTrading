"""
position.py

Represents a single portfolio position.

The Position class is responsible for maintaining:

- Current quantity
- Average cost
- Market value
- Realized PnL
- Unrealized PnL

Only executed trades modify a Position.
"""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal

from broker.trade import Trade


@dataclass(slots=True)
class Position:
    """
    Represents one open position.
    """

    symbol: str

    quantity: int = 0

    average_cost: Decimal = Decimal("0")

    market_price: Decimal = Decimal("0")

    realized_pnl: Decimal = Decimal("0")

    def __post_init__(self) -> None:

        self.symbol = self.symbol.upper().strip()

        if not self.symbol:
            raise ValueError("Symbol cannot be empty.")

    # ---------------------------------------------------------
    # Trade Processing
    # ---------------------------------------------------------

    def apply_trade(
        self,
        trade: Trade,
    ) -> None:
        """
        Apply an executed trade.

        BUY:
            Increases position size and updates average cost.

        SELL:
            Realizes PnL and reduces position.
        """

        if trade.symbol != self.symbol:
            raise ValueError(
                "Trade symbol does not match position."
            )

        if trade.is_buy:
            self._apply_buy(trade)
        else:
            self._apply_sell(trade)

    def _apply_buy(
        self,
        trade: Trade,
    ) -> None:

        existing_cost = (
            self.average_cost * self.quantity
        )

        purchase_cost = (
            trade.gross_value + trade.commission
        )

        new_quantity = (
            self.quantity + trade.quantity
        )

        self.average_cost = (
            existing_cost + purchase_cost
        ) / Decimal(new_quantity)

        self.quantity = new_quantity

    def _apply_sell(
        self,
        trade: Trade,
    ) -> None:

        if trade.quantity > self.quantity:
            raise ValueError(
                "Cannot sell more than current position."
            )

        proceeds = (
            trade.gross_value - trade.commission
        )

        cost_basis = (
            self.average_cost * trade.quantity
        )

        self.realized_pnl += (
            proceeds - cost_basis
        )

        self.quantity -= trade.quantity

        if self.quantity == 0:

            self.average_cost = Decimal("0")
            self.market_price = Decimal("0")

    # ---------------------------------------------------------
    # Market Data
    # ---------------------------------------------------------

    def update_market_price(
        self,
        price: Decimal,
    ) -> None:

        price = Decimal(price)

        if price <= 0:
            raise ValueError(
                "Market price must be positive."
            )

        self.market_price = price

    # ---------------------------------------------------------
    # Properties
    # ---------------------------------------------------------

    @property
    def market_value(self) -> Decimal:

        return (
            Decimal(self.quantity)
            * self.market_price
        )

    @property
    def cost_basis(self) -> Decimal:

        return (
            Decimal(self.quantity)
            * self.average_cost
        )

    @property
    def unrealized_pnl(self) -> Decimal:

        return (
            self.market_value
            - self.cost_basis
        )

    @property
    def total_pnl(self) -> Decimal:

        return (
            self.realized_pnl
            + self.unrealized_pnl
        )

    @property
    def is_open(self) -> bool:

        return self.quantity > 0

    # ---------------------------------------------------------

    def __repr__(self) -> str:

        return (
            "Position("
            f"symbol={self.symbol}, "
            f"qty={self.quantity}, "
            f"avg_cost={self.average_cost}, "
            f"market_price={self.market_price}, "
            f"realized_pnl={self.realized_pnl}, "
            f"unrealized_pnl={self.unrealized_pnl}, "
            f"market_value={self.market_value}"
            ")"
        )