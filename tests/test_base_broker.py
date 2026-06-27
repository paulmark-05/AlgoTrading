"""
Tests for broker.base_broker
"""

from decimal import Decimal

import pytest

from broker.base_broker import BaseBroker
from broker.execution_report import ExecutionReport
from broker.order import Order
from broker.portfolio import Portfolio


class DummyBroker(BaseBroker):
    """
    Minimal concrete implementation used solely for testing
    BaseBroker.
    """

    def __init__(self):
        self._connected = False
        self._portfolio = Portfolio(
            initial_cash=Decimal("10000")
        )

    # --------------------------------------------------
    # Connection
    # --------------------------------------------------

    def connect(self):
        self._connected = True

    def disconnect(self):
        self._connected = False

    @property
    def is_connected(self):
        return self._connected

    # --------------------------------------------------
    # Orders
    # --------------------------------------------------

    def place_order(
        self,
        order: Order,
    ) -> ExecutionReport:
        raise NotImplementedError

    def cancel_order(
        self,
        order_id: str,
    ) -> bool:
        return False

    def get_order(
        self,
        order_id: str,
    ):
        return None

    def get_open_orders(self):
        return []

    # --------------------------------------------------
    # Portfolio
    # --------------------------------------------------

    @property
    def portfolio(self):
        return self._portfolio

    # --------------------------------------------------
    # Market Data
    # --------------------------------------------------

    def update_market_price(
        self,
        symbol,
        price,
    ):
        pass


# ======================================================
# Tests
# ======================================================


def test_base_broker_is_abstract():
    """
    BaseBroker should not be instantiable.
    """

    with pytest.raises(TypeError):
        BaseBroker()


def test_connect_disconnect():

    broker = DummyBroker()

    assert broker.is_connected is False

    broker.connect()

    assert broker.is_connected is True

    broker.disconnect()

    assert broker.is_connected is False


def test_cash_property():

    broker = DummyBroker()

    assert broker.cash == Decimal("10000")


def test_positions_property():

    broker = DummyBroker()

    assert broker.positions == {}


def test_portfolio_property():

    broker = DummyBroker()

    assert isinstance(
        broker.portfolio,
        Portfolio,
    )


def test_get_open_orders_returns_empty_list():

    broker = DummyBroker()

    assert broker.get_open_orders() == []


def test_get_order_returns_none():

    broker = DummyBroker()

    assert broker.get_order("ABC") is None


def test_cancel_order_returns_false():

    broker = DummyBroker()

    assert broker.cancel_order("ABC") is False


def test_update_market_price_does_not_raise():

    broker = DummyBroker()

    broker.update_market_price(
        "AAPL",
        Decimal("185.25"),
    )