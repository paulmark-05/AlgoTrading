"""
base_broker.py

Abstract broker interface.

All broker implementations (paper trading, backtesting, live brokers)
should inherit from BaseBroker.

Strategies should depend only on this interface.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from decimal import Decimal

from broker.execution_report import ExecutionReport
from broker.order import Order
from broker.portfolio import Portfolio


class BaseBroker(ABC):
    """
    Abstract broker interface.
    """

    # ---------------------------------------------------------
    # Connection
    # ---------------------------------------------------------

    @abstractmethod
    def connect(self) -> None:
        """
        Connect to the broker.
        """
        ...

    @abstractmethod
    def disconnect(self) -> None:
        """
        Disconnect from the broker.
        """
        ...

    # ---------------------------------------------------------
    # Orders
    # ---------------------------------------------------------

    @abstractmethod
    def place_order(
        self,
        order: Order,
    ) -> ExecutionReport:
        """
        Submit an order.

        Returns an ExecutionReport describing the outcome.
        """
        ...

    @abstractmethod
    def cancel_order(
        self,
        order_id: str,
    ) -> bool:
        """
        Cancel a pending order.

        Returns True if cancelled.
        """
        ...

    @abstractmethod
    def get_order(
        self,
        order_id: str,
    ) -> Order | None:
        """
        Retrieve an order by ID.
        """
        ...

    @abstractmethod
    def get_open_orders(
        self,
    ) -> list[Order]:
        """
        Return all currently open orders.
        """
        ...

    # ---------------------------------------------------------
    # Portfolio
    # ---------------------------------------------------------

    @property
    @abstractmethod
    def portfolio(
        self,
    ) -> Portfolio:
        """
        Portfolio owned by the broker.
        """
        ...

    @property
    def cash(self) -> Decimal:
        """
        Convenience accessor.
        """
        return self.portfolio.cash

    @property
    def positions(self):
        """
        Convenience accessor.
        """
        return self.portfolio.positions

    # ---------------------------------------------------------
    # Market Data
    # ---------------------------------------------------------

    @abstractmethod
    def update_market_price(
        self,
        symbol: str,
        price: Decimal | float | int,
    ) -> None:
        """
        Update the latest market price.

        Paper brokers use this to:

        - value positions
        - execute limit orders
        - execute stop orders
        """
        ...

    # ---------------------------------------------------------
    # State
    # ---------------------------------------------------------

    @property
    @abstractmethod
    def is_connected(self) -> bool:
        """
        True if broker is connected.
        """
        ...