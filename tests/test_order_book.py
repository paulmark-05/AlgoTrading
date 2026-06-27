"""
Tests for broker.order_book
"""

from decimal import Decimal

import pytest

from broker.enums import (
    OrderSide,
    OrderStatus,
    OrderType,
)
from broker.exceptions import (
    DuplicateOrderError,
    OrderNotFoundError,
)
from broker.order import Order
from broker.order_book import OrderBook


def make_order(order_id: str) -> Order:

    return Order(
        order_id=order_id,
        symbol="NIFTY",
        side=OrderSide.BUY,
        quantity=10,
        order_type=OrderType.MARKET,
    )


def test_new_order_book():

    book = OrderBook()

    assert len(book) == 0


def test_add_order():

    book = OrderBook()

    order = make_order("ORD-001")

    book.add(order)

    assert len(book) == 1
    assert book.has_order("ORD-001")


def test_get_order():

    book = OrderBook()

    order = make_order("ORD-001")

    book.add(order)

    assert book.get("ORD-001") is order


def test_duplicate_order():

    book = OrderBook()

    order = make_order("ORD-001")

    book.add(order)

    with pytest.raises(DuplicateOrderError):
        book.add(order)


def test_remove_order():

    book = OrderBook()

    order = make_order("ORD-001")

    book.add(order)

    removed = book.remove("ORD-001")

    assert removed is order
    assert len(book) == 0


def test_remove_unknown_order():

    book = OrderBook()

    with pytest.raises(OrderNotFoundError):
        book.remove("UNKNOWN")


def test_get_unknown_order():

    book = OrderBook()

    with pytest.raises(OrderNotFoundError):
        book.get("UNKNOWN")


def test_mark_filled():

    book = OrderBook()

    order = make_order("ORD-001")

    book.add(order)

    book.mark_filled("ORD-001")

    assert order.status == OrderStatus.FILLED


def test_mark_partial():

    book = OrderBook()

    order = make_order("ORD-001")

    book.add(order)

    book.mark_partial("ORD-001")

    assert order.status == OrderStatus.PARTIALLY_FILLED


def test_mark_cancelled():

    book = OrderBook()

    order = make_order("ORD-001")

    book.add(order)

    book.mark_cancelled("ORD-001")

    assert order.status == OrderStatus.CANCELLED


def test_mark_rejected():

    book = OrderBook()

    order = make_order("ORD-001")

    book.add(order)

    book.mark_rejected("ORD-001")

    assert order.status == OrderStatus.REJECTED


def test_open_orders():

    book = OrderBook()

    a = make_order("A")
    b = make_order("B")
    c = make_order("C")

    book.add(a)
    book.add(b)
    book.add(c)

    book.mark_filled("B")

    open_orders = book.open_orders()

    assert len(open_orders) == 2
    assert a in open_orders
    assert c in open_orders


def test_completed_orders():

    book = OrderBook()

    a = make_order("A")
    b = make_order("B")
    c = make_order("C")

    book.add(a)
    book.add(b)
    book.add(c)

    book.mark_filled("A")
    book.mark_cancelled("B")

    completed = book.completed_orders()

    assert len(completed) == 2
    assert a in completed
    assert b in completed


def test_clear():

    book = OrderBook()

    book.add(make_order("A"))
    book.add(make_order("B"))

    assert len(book) == 2

    book.clear()

    assert len(book) == 0


def test_contains():

    book = OrderBook()

    order = make_order("ORD-001")

    book.add(order)

    assert "ORD-001" in book
    assert "UNKNOWN" not in book


def test_iteration():

    book = OrderBook()

    a = make_order("A")
    b = make_order("B")

    book.add(a)
    book.add(b)

    orders = list(book)

    assert len(orders) == 2
    assert a in orders
    assert b in orders