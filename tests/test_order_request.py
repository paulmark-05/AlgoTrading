from decimal import Decimal

import pytest

from broker.enums import OrderType
from engine.order_request import OrderRequest


def test_order_request_creation():

    request = OrderRequest(
        symbol="nifty",
        quantity=10,
    )

    assert request.symbol == "NIFTY"
    assert request.quantity == 10
    assert request.order_type == OrderType.MARKET


def test_empty_symbol_rejected():

    with pytest.raises(ValueError):
        OrderRequest(
            symbol="",
            quantity=10,
        )


def test_invalid_quantity_rejected():

    with pytest.raises(ValueError):
        OrderRequest(
            symbol="NIFTY",
            quantity=0,
        )


def test_price_normalized():

    request = OrderRequest(
        symbol="NIFTY",
        quantity=10,
        order_type=OrderType.LIMIT,
        price=Decimal("22500"),
    )

    assert request.price == Decimal("22500")


def test_invalid_price_rejected():

    with pytest.raises(ValueError):
        OrderRequest(
            symbol="NIFTY",
            quantity=10,
            price=Decimal("0"),
        )