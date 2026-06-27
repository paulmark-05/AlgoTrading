"""
Tests for broker.trade
"""

from decimal import Decimal

import pytest

from broker.enums import OrderSide
from broker.trade import Trade


def test_buy_trade_creation():
    trade = Trade(
        trade_id="TRD-001",
        order_id="ORD-001",
        symbol="nifty",
        side=OrderSide.BUY,
        quantity=10,
        price=Decimal("100"),
        commission=Decimal("5"),
    )

    assert trade.trade_id == "TRD-001"
    assert trade.order_id == "ORD-001"
    assert trade.symbol == "NIFTY"
    assert trade.side == OrderSide.BUY
    assert trade.quantity == 10
    assert trade.price == Decimal("100")
    assert trade.commission == Decimal("5")
    assert trade.is_buy is True
    assert trade.is_sell is False


def test_sell_trade_creation():
    trade = Trade(
        trade_id="TRD-002",
        order_id="ORD-002",
        symbol="NIFTY",
        side=OrderSide.SELL,
        quantity=5,
        price=Decimal("120"),
    )

    assert trade.is_buy is False
    assert trade.is_sell is True
    assert trade.commission == Decimal("0")


def test_gross_value():
    trade = Trade(
        trade_id="TRD-003",
        order_id="ORD-003",
        symbol="NIFTY",
        side=OrderSide.BUY,
        quantity=10,
        price=Decimal("100"),
    )

    assert trade.gross_value == Decimal("1000")


def test_buy_net_value_includes_commission():
    trade = Trade(
        trade_id="TRD-004",
        order_id="ORD-004",
        symbol="NIFTY",
        side=OrderSide.BUY,
        quantity=10,
        price=Decimal("100"),
        commission=Decimal("5"),
    )

    assert trade.net_value == Decimal("1005")


def test_sell_net_value_deducts_commission():
    trade = Trade(
        trade_id="TRD-005",
        order_id="ORD-005",
        symbol="NIFTY",
        side=OrderSide.SELL,
        quantity=10,
        price=Decimal("100"),
        commission=Decimal("5"),
    )

    assert trade.net_value == Decimal("995")


def test_empty_symbol_rejected():
    with pytest.raises(ValueError):
        Trade(
            trade_id="TRD-006",
            order_id="ORD-006",
            symbol="",
            side=OrderSide.BUY,
            quantity=10,
            price=Decimal("100"),
        )


def test_zero_quantity_rejected():
    with pytest.raises(ValueError):
        Trade(
            trade_id="TRD-007",
            order_id="ORD-007",
            symbol="NIFTY",
            side=OrderSide.BUY,
            quantity=0,
            price=Decimal("100"),
        )


def test_negative_price_rejected():
    with pytest.raises(ValueError):
        Trade(
            trade_id="TRD-008",
            order_id="ORD-008",
            symbol="NIFTY",
            side=OrderSide.BUY,
            quantity=10,
            price=Decimal("-1"),
        )


def test_negative_commission_rejected():
    with pytest.raises(ValueError):
        Trade(
            trade_id="TRD-009",
            order_id="ORD-009",
            symbol="NIFTY",
            side=OrderSide.BUY,
            quantity=10,
            price=Decimal("100"),
            commission=Decimal("-1"),
        )


def test_trade_is_immutable():
    trade = Trade(
        trade_id="TRD-010",
        order_id="ORD-010",
        symbol="NIFTY",
        side=OrderSide.BUY,
        quantity=10,
        price=Decimal("100"),
    )

    with pytest.raises(Exception):
        trade.price = Decimal("200")