"""
Phase 1 tests for broker.paper_broker

Scope:
- construction
- initial broker state
- market price cache
- basic portfolio access
"""

from decimal import Decimal

from broker.paper_broker import PaperBroker


def test_paper_broker_creation():

    broker = PaperBroker(
        initial_cash=Decimal("100000")
    )

    assert broker is not None


def test_initial_cash():

    broker = PaperBroker(
        initial_cash=Decimal("100000")
    )

    assert broker.cash == Decimal("100000")


def test_initial_books_are_empty():

    broker = PaperBroker(
        initial_cash=Decimal("100000")
    )

    assert len(broker.order_book) == 0
    assert len(broker.trade_book) == 0
    assert broker.execution_reports == []


def test_initial_market_prices_empty():

    broker = PaperBroker(
        initial_cash=Decimal("100000")
    )

    assert broker.market_prices == {}


def test_initial_positions_empty():

    broker = PaperBroker(
        initial_cash=Decimal("100000")
    )

    assert broker.positions() == {}


def test_commission_settings():

    broker = PaperBroker(
        initial_cash=Decimal("100000"),
        commission_per_share=Decimal("2"),
        minimum_commission=Decimal("20"),
    )

    assert broker.commission_per_share == Decimal("2")
    assert broker.minimum_commission == Decimal("20")


def test_update_market_price_stores_price():

    broker = PaperBroker(
        initial_cash=Decimal("100000")
    )

    broker.update_market_price(
        "NIFTY",
        Decimal("22500"),
    )

    assert broker.market_prices["NIFTY"] == Decimal("22500")


def test_get_market_price():

    broker = PaperBroker(
        initial_cash=Decimal("100000")
    )

    broker.update_market_price(
        "NIFTY",
        Decimal("22500"),
    )

    assert broker.get_market_price("NIFTY") == Decimal("22500")


def test_get_missing_market_price_raises():

    broker = PaperBroker(
        initial_cash=Decimal("100000")
    )

    try:
        broker.get_market_price("NIFTY")
        assert False, "Expected ValueError"
    except ValueError:
        pass

from broker.enums import OrderSide, OrderType
from broker.order import Order


def test_submit_buy_market_order_executes_trade():

    broker = PaperBroker(
        initial_cash=Decimal("100000")
    )

    order = Order(
        symbol="NIFTY",
        side=OrderSide.BUY,
        quantity=10,
        order_type=OrderType.MARKET,
    )

    trade = broker.submit_order(
        order,
        market_price=Decimal("100"),
    )

    assert trade is not None
    assert len(broker.order_book) == 1
    assert len(broker.trade_book) == 1
    assert broker.cash == Decimal("99000")
    assert broker.has_position("NIFTY") is True

    position = broker.get_position("NIFTY")

    assert position.quantity == 10
    assert position.average_cost == Decimal("100")
    assert order.is_filled is True


def test_submit_buy_market_order_records_execution_reports():

    broker = PaperBroker(
        initial_cash=Decimal("100000")
    )

    order = Order(
        symbol="NIFTY",
        side=OrderSide.BUY,
        quantity=10,
        order_type=OrderType.MARKET,
    )

    broker.submit_order(
        order,
        market_price=Decimal("100"),
    )

    reports = broker.executions()

    assert len(reports) == 2
    assert reports[0].order_id == order.order_id
    assert reports[1].order_id == order.order_id


def test_submit_buy_market_order_records_trade():

    broker = PaperBroker(
        initial_cash=Decimal("100000")
    )

    order = Order(
        symbol="NIFTY",
        side=OrderSide.BUY,
        quantity=10,
        order_type=OrderType.MARKET,
    )

    trade = broker.submit_order(
        order,
        market_price=Decimal("100"),
    )

    trades = list(broker.trades())

    assert len(trades) == 1
    assert trades[0] is trade
    assert trade.symbol == "NIFTY"
    assert trade.side == OrderSide.BUY
    assert trade.quantity == 10
    assert trade.price == Decimal("100")

def test_submit_sell_market_order_partial_exit():

    broker = PaperBroker(
        initial_cash=Decimal("100000")
    )

    buy_order = Order(
        symbol="NIFTY",
        side=OrderSide.BUY,
        quantity=10,
        order_type=OrderType.MARKET,
    )

    broker.submit_order(
        buy_order,
        market_price=Decimal("100"),
    )

    sell_order = Order(
        symbol="NIFTY",
        side=OrderSide.SELL,
        quantity=4,
        order_type=OrderType.MARKET,
    )

    trade = broker.submit_order(
        sell_order,
        market_price=Decimal("120"),
    )

    assert trade is not None
    assert broker.cash == Decimal("99480")

    position = broker.get_position("NIFTY")

    assert position.quantity == 6
    assert position.average_cost == Decimal("100")
    assert position.realized_pnl == Decimal("80")


def test_submit_sell_market_order_full_exit():

    broker = PaperBroker(
        initial_cash=Decimal("100000")
    )

    buy_order = Order(
        symbol="NIFTY",
        side=OrderSide.BUY,
        quantity=10,
        order_type=OrderType.MARKET,
    )

    broker.submit_order(
        buy_order,
        market_price=Decimal("100"),
    )

    sell_order = Order(
        symbol="NIFTY",
        side=OrderSide.SELL,
        quantity=10,
        order_type=OrderType.MARKET,
    )

    trade = broker.submit_order(
        sell_order,
        market_price=Decimal("120"),
    )

    assert trade is not None
    assert broker.cash == Decimal("100200")
    assert broker.has_position("NIFTY") is False
    assert broker.realized_pnl == Decimal("200")
    assert sell_order.is_filled is True

import pytest

def test_buy_order_rejected_for_insufficient_cash():

    broker = PaperBroker(
        initial_cash=Decimal("500")
    )

    order = Order(
        symbol="NIFTY",
        side=OrderSide.BUY,
        quantity=10,
        order_type=OrderType.MARKET,
    )

    with pytest.raises(ValueError):
        broker.submit_order(
            order,
            market_price=Decimal("100"),
        )


def test_sell_order_rejected_without_position():

    broker = PaperBroker(
        initial_cash=Decimal("100000")
    )

    order = Order(
        symbol="NIFTY",
        side=OrderSide.SELL,
        quantity=10,
        order_type=OrderType.MARKET,
    )

    with pytest.raises(ValueError):
        broker.submit_order(
            order,
            market_price=Decimal("100"),
        )


def test_sell_order_rejected_when_overselling():

    broker = PaperBroker(
        initial_cash=Decimal("100000")
    )

    buy_order = Order(
        symbol="NIFTY",
        side=OrderSide.BUY,
        quantity=5,
        order_type=OrderType.MARKET,
    )

    broker.submit_order(
        buy_order,
        market_price=Decimal("100"),
    )

    sell_order = Order(
        symbol="NIFTY",
        side=OrderSide.SELL,
        quantity=10,
        order_type=OrderType.MARKET,
    )

    with pytest.raises(ValueError):
        broker.submit_order(
            sell_order,
            market_price=Decimal("100"),
        )

def test_market_update_changes_position_market_price():

    broker = PaperBroker(
        initial_cash=Decimal("100000")
    )

    order = Order(
        symbol="NIFTY",
        side=OrderSide.BUY,
        quantity=10,
        order_type=OrderType.MARKET,
    )

    broker.submit_order(
        order,
        market_price=Decimal("100"),
    )

    broker.update_market_price(
        "NIFTY",
        Decimal("130"),
    )

    position = broker.get_position("NIFTY")

    assert position.market_price == Decimal("130")


def test_market_update_changes_market_value():

    broker = PaperBroker(
        initial_cash=Decimal("100000")
    )

    order = Order(
        symbol="NIFTY",
        side=OrderSide.BUY,
        quantity=10,
        order_type=OrderType.MARKET,
    )

    broker.submit_order(
        order,
        market_price=Decimal("100"),
    )

    broker.update_market_price(
        "NIFTY",
        Decimal("130"),
    )

    assert broker.market_value == Decimal("1300")


def test_market_update_changes_unrealized_pnl():

    broker = PaperBroker(
        initial_cash=Decimal("100000")
    )

    order = Order(
        symbol="NIFTY",
        side=OrderSide.BUY,
        quantity=10,
        order_type=OrderType.MARKET,
    )

    broker.submit_order(
        order,
        market_price=Decimal("100"),
    )

    broker.update_market_price(
        "NIFTY",
        Decimal("130"),
    )

    assert broker.unrealized_pnl == Decimal("300")


def test_market_update_changes_total_pnl():

    broker = PaperBroker(
        initial_cash=Decimal("100000")
    )

    order = Order(
        symbol="NIFTY",
        side=OrderSide.BUY,
        quantity=10,
        order_type=OrderType.MARKET,
    )

    broker.submit_order(
        order,
        market_price=Decimal("100"),
    )

    broker.update_market_price(
        "NIFTY",
        Decimal("130"),
    )

    assert broker.total_pnl == Decimal("300")


def test_get_order_returns_submitted_order():

    broker = PaperBroker(
        initial_cash=Decimal("100000")
    )

    order = Order(
        symbol="NIFTY",
        side=OrderSide.BUY,
        quantity=10,
        order_type=OrderType.MARKET,
    )

    broker.submit_order(
        order,
        market_price=Decimal("100"),
    )

    assert broker.get_order(order.order_id) is order


def test_filled_orders_returns_filled_order():

    broker = PaperBroker(
        initial_cash=Decimal("100000")
    )

    order = Order(
        symbol="NIFTY",
        side=OrderSide.BUY,
        quantity=10,
        order_type=OrderType.MARKET,
    )

    broker.submit_order(
        order,
        market_price=Decimal("100"),
    )

    filled = broker.filled_orders()

    assert len(filled) == 1
    assert filled[0] is order


def test_submit_resting_order_without_market_price():

    broker = PaperBroker(
        initial_cash=Decimal("100000")
    )

    order = Order(
        symbol="NIFTY",
        side=OrderSide.BUY,
        quantity=10,
        order_type=OrderType.MARKET,
    )

    result = broker.submit_order(order)

    assert result is None
    assert broker.get_order(order.order_id) is order
    assert order.is_open is True
    assert len(broker.open_orders()) == 1


def test_cancel_resting_order():

    broker = PaperBroker(
        initial_cash=Decimal("100000")
    )

    order = Order(
        symbol="NIFTY",
        side=OrderSide.BUY,
        quantity=10,
        order_type=OrderType.MARKET,
    )

    broker.submit_order(order)

    broker.cancel_order(order.order_id)

    assert order.is_cancelled is True
    assert len(broker.open_orders()) == 0


def test_cancel_filled_order_raises():

    broker = PaperBroker(
        initial_cash=Decimal("100000")
    )

    order = Order(
        symbol="NIFTY",
        side=OrderSide.BUY,
        quantity=10,
        order_type=OrderType.MARKET,
    )

    broker.submit_order(
        order,
        market_price=Decimal("100"),
    )

    with pytest.raises(ValueError):
        broker.cancel_order(order.order_id)


def test_reset_clears_broker_state():

    broker = PaperBroker(
        initial_cash=Decimal("100000")
    )

    order = Order(
        symbol="NIFTY",
        side=OrderSide.BUY,
        quantity=10,
        order_type=OrderType.MARKET,
    )

    broker.submit_order(
        order,
        market_price=Decimal("100"),
    )

    broker.update_market_price(
        "NIFTY",
        Decimal("130"),
    )

    broker.reset()

    assert len(broker.order_book) == 0
    assert len(broker.trade_book) == 0
    assert broker.execution_reports == []
    assert broker.market_prices == {}
    assert broker.positions() == {}

