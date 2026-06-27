"""
Tests for broker.position
"""

from decimal import Decimal

import pytest

from broker.enums import OrderSide
from broker.position import Position
from broker.trade import Trade


def make_buy_trade(
    qty: int,
    price: str,
    commission: str = "0",
):
    return Trade(
        trade_id="TRD-BUY",
        order_id="ORD-BUY",
        symbol="NIFTY",
        side=OrderSide.BUY,
        quantity=qty,
        price=Decimal(price),
        commission=Decimal(commission),
    )


def make_sell_trade(
    qty: int,
    price: str,
    commission: str = "0",
):
    return Trade(
        trade_id="TRD-SELL",
        order_id="ORD-SELL",
        symbol="NIFTY",
        side=OrderSide.SELL,
        quantity=qty,
        price=Decimal(price),
        commission=Decimal(commission),
    )


def test_new_position():

    position = Position("NIFTY")

    assert position.symbol == "NIFTY"
    assert position.quantity == 0
    assert position.average_cost == Decimal("0")
    assert position.market_price == Decimal("0")
    assert position.realized_pnl == Decimal("0")
    assert position.is_open is False


def test_buy_trade_creates_position():

    position = Position("NIFTY")

    trade = make_buy_trade(10, "100")

    position.apply_trade(trade)

    assert position.quantity == 10
    assert position.average_cost == Decimal("100")
    assert position.is_open is True


def test_multiple_buys_average_cost():

    position = Position("NIFTY")

    position.apply_trade(
        make_buy_trade(10, "100")
    )

    position.apply_trade(
        make_buy_trade(10, "120")
    )

    assert position.quantity == 20
    assert position.average_cost == Decimal("110")


def test_market_price_update():

    position = Position("NIFTY")

    position.apply_trade(
        make_buy_trade(10, "100")
    )

    position.update_market_price(
        Decimal("120")
    )

    assert position.market_price == Decimal("120")


def test_market_value():

    position = Position("NIFTY")

    position.apply_trade(
        make_buy_trade(10, "100")
    )

    position.update_market_price(
        Decimal("120")
    )

    assert position.market_value == Decimal("1200")


def test_unrealized_pnl():

    position = Position("NIFTY")

    position.apply_trade(
        make_buy_trade(10, "100")
    )

    position.update_market_price(
        Decimal("120")
    )

    assert position.unrealized_pnl == Decimal("200")


def test_partial_sell():

    position = Position("NIFTY")

    position.apply_trade(
        make_buy_trade(10, "100")
    )

    position.apply_trade(
        make_sell_trade(5, "120")
    )

    assert position.quantity == 5
    assert position.realized_pnl == Decimal("100")


def test_complete_exit():

    position = Position("NIFTY")

    position.apply_trade(
        make_buy_trade(10, "100")
    )

    position.apply_trade(
        make_sell_trade(10, "120")
    )

    assert position.quantity == 0
    assert position.average_cost == Decimal("0")
    assert position.market_price == Decimal("0")
    assert position.is_open is False


def test_sell_more_than_position():

    position = Position("NIFTY")

    position.apply_trade(
        make_buy_trade(5, "100")
    )

    with pytest.raises(ValueError):
        position.apply_trade(
            make_sell_trade(10, "120")
        )


def test_trade_symbol_mismatch():

    position = Position("NIFTY")

    trade = Trade(
        trade_id="TRD-001",
        order_id="ORD-001",
        symbol="BANKNIFTY",
        side=OrderSide.BUY,
        quantity=1,
        price=Decimal("100"),
    )

    with pytest.raises(ValueError):
        position.apply_trade(trade)


def test_negative_market_price():

    position = Position("NIFTY")

    with pytest.raises(ValueError):
        position.update_market_price(
            Decimal("-1")
        )


def test_repr():

    position = Position("NIFTY")

    text = repr(position)

    assert "Position(" in text
    assert "NIFTY" in text