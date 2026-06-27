"""
Tests for broker.portfolio
"""

from decimal import Decimal

import pytest

from broker.enums import OrderSide
from broker.portfolio import Portfolio
from broker.trade import Trade


def buy_trade(
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


def sell_trade(
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


def test_new_portfolio():

    portfolio = Portfolio(
        initial_cash=Decimal("100000")
    )

    assert portfolio.cash == Decimal("100000")
    assert len(portfolio) == 0
    assert portfolio.positions == {}
    assert portfolio.market_value == Decimal("0")
    assert portfolio.total_value == Decimal("100000")


def test_negative_initial_cash():

    with pytest.raises(ValueError):
        Portfolio(
            initial_cash=Decimal("-1")
        )


def test_buy_trade_reduces_cash():

    portfolio = Portfolio(
        Decimal("100000")
    )

    portfolio.apply_trade(
        buy_trade(10, "100")
    )

    assert portfolio.cash == Decimal("99000")


def test_buy_creates_position():

    portfolio = Portfolio(
        Decimal("100000")
    )

    portfolio.apply_trade(
        buy_trade(10, "100")
    )

    assert portfolio.has_position(
        "NIFTY"
    )

    position = portfolio.get_position(
        "NIFTY"
    )

    assert position.quantity == 10


def test_sell_increases_cash():

    portfolio = Portfolio(
        Decimal("100000")
    )

    portfolio.apply_trade(
        buy_trade(10, "100")
    )

    portfolio.apply_trade(
        sell_trade(10, "120")
    )

    assert portfolio.cash == Decimal("100200")


def test_position_removed_after_exit():

    portfolio = Portfolio(
        Decimal("100000")
    )

    portfolio.apply_trade(
        buy_trade(10, "100")
    )

    portfolio.apply_trade(
        sell_trade(10, "100")
    )

    assert not portfolio.has_position(
        "NIFTY"
    )

    assert len(portfolio) == 0


def test_market_price_update():

    portfolio = Portfolio(
        Decimal("100000")
    )

    portfolio.apply_trade(
        buy_trade(10, "100")
    )

    portfolio.update_market_price(
        "NIFTY",
        Decimal("120")
    )

    position = portfolio.get_position(
        "NIFTY"
    )

    assert position.market_price == Decimal(
        "120"
    )


def test_market_value():

    portfolio = Portfolio(
        Decimal("100000")
    )

    portfolio.apply_trade(
        buy_trade(10, "100")
    )

    portfolio.update_market_price(
        "NIFTY",
        Decimal("120")
    )

    assert portfolio.market_value == Decimal(
        "1200"
    )


def test_total_value():

    portfolio = Portfolio(
        Decimal("100000")
    )

    portfolio.apply_trade(
        buy_trade(10, "100")
    )

    portfolio.update_market_price(
        "NIFTY",
        Decimal("120")
    )

    assert portfolio.total_value == Decimal(
        "100200"
    )


def test_unrealized_pnl():

    portfolio = Portfolio(
        Decimal("100000")
    )

    portfolio.apply_trade(
        buy_trade(10, "100")
    )

    portfolio.update_market_price(
        "NIFTY",
        Decimal("120")
    )

    assert portfolio.unrealized_pnl == Decimal(
        "200"
    )


def test_realized_pnl():

    portfolio = Portfolio(
        Decimal("100000")
    )

    portfolio.apply_trade(
        buy_trade(10, "100")
    )

    portfolio.apply_trade(
        sell_trade(10, "120")
    )

    assert portfolio.realized_pnl == Decimal(
        "200"
    )


def test_reset():

    portfolio = Portfolio(
        Decimal("100000")
    )

    portfolio.apply_trade(
        buy_trade(10, "100")
    )

    portfolio.reset()

    assert len(portfolio) == 0
    assert portfolio.positions == {}


def test_contains():

    portfolio = Portfolio(
        Decimal("100000")
    )

    portfolio.apply_trade(
        buy_trade(10, "100")
    )

    assert "NIFTY" in portfolio
    assert "BANKNIFTY" not in portfolio


def test_repr():

    portfolio = Portfolio(
        Decimal("100000")
    )

    text = repr(portfolio)

    assert "Portfolio(" in text
    