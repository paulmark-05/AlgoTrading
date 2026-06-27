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
    def __init__(self):
        self._connected = False
        self._portfolio = Portfolio(
            initial_cash=Decimal("10000")
        )

    def connect(self) -> None:
        self._connected = True

    def disconnect(self) -> None:
        self._connected = False

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
    ) -> Order | None:
        return None

    def get_open_orders(self) -> list[Order]:
        return []

    @property
    def portfolio(self) -> Portfolio:
        return self._portfolio

    def update_market_price(
        self,
        symbol: str,
        price: Decimal | float | int,
    ) -> None:
        return None

    @property
    def is_connected(self) -> bool:
        return self._connected


def test_base_broker_is_abstract():
    with pytest.raises(TypeError):
        BaseBroker()


def test_dummy_broker_can_be_instantiated():
    broker = DummyBroker()
    assert broker is not None


def test_connect_disconnect():
    broker = DummyBroker()

    assert broker.is_connected is False

    broker.connect()
    assert broker.is_connected is True

    broker.disconnect()
    assert broker.is_connected is False


def test_cash_property_delegates_to_portfolio():
    broker = DummyBroker()

    assert broker.cash == Decimal("10000")


def test_positions_property_delegates_to_portfolio():
    broker = DummyBroker()

    assert broker.positions == {}


def test_get_order_returns_none_for_missing_order():
    broker = DummyBroker()

    assert broker.get_order("UNKNOWN") is None


def test_get_open_orders_returns_empty_list():
    broker = DummyBroker()

    assert broker.get_open_orders() == []


def test_cancel_unknown_order_returns_false():
    broker = DummyBroker()

    assert broker.cancel_order("UNKNOWN") is False


def test_update_market_price_does_not_raise():
    broker = DummyBroker()

    broker.update_market_price(
        "NIFTY",
        Decimal("22500"),
    )