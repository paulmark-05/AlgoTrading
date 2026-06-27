"""
Tests for broker.trade_book
"""

from decimal import Decimal

import pytest

from broker.enums import OrderSide
from broker.exceptions import (
    DuplicateTradeError,
    TradeNotFoundError,
)
from broker.trade import Trade
from broker.trade_book import TradeBook


def make_trade(trade_id: str) -> Trade:
    return Trade(
        trade_id=trade_id,
        order_id=f"ORD-{trade_id}",
        symbol="NIFTY",
        side=OrderSide.BUY,
        quantity=10,
        price=Decimal("100"),
    )


def test_new_trade_book():
    book = TradeBook()

    assert len(book) == 0


def test_add_trade():
    book = TradeBook()

    trade = make_trade("TRD-001")

    book.add(trade)

    assert len(book) == 1
    assert book.has_trade("TRD-001")


def test_get_trade():
    book = TradeBook()

    trade = make_trade("TRD-001")

    book.add(trade)

    assert book.get("TRD-001") is trade


def test_duplicate_trade():
    book = TradeBook()

    trade = make_trade("TRD-001")

    book.add(trade)

    with pytest.raises(DuplicateTradeError):
        book.add(trade)


def test_remove_trade():
    book = TradeBook()

    trade = make_trade("TRD-001")

    book.add(trade)

    removed = book.remove("TRD-001")

    assert removed is trade
    assert len(book) == 0


def test_remove_unknown_trade():
    book = TradeBook()

    with pytest.raises(TradeNotFoundError):
        book.remove("UNKNOWN")


def test_get_unknown_trade():
    book = TradeBook()

    with pytest.raises(TradeNotFoundError):
        book.get("UNKNOWN")


def test_all_trades():
    book = TradeBook()

    a = make_trade("A")
    b = make_trade("B")

    book.add(a)
    book.add(b)

    trades = book.all_trades()

    assert len(trades) == 2
    assert a in trades
    assert b in trades


def test_trades_for_symbol():
    book = TradeBook()

    nifty = make_trade("A")

    banknifty = Trade(
        trade_id="B",
        order_id="ORD-B",
        symbol="BANKNIFTY",
        side=OrderSide.BUY,
        quantity=5,
        price=Decimal("200"),
    )

    book.add(nifty)
    book.add(banknifty)

    trades = book.trades_for_symbol("NIFTY")

    assert len(trades) == 1
    assert trades[0] is nifty


def test_values():
    book = TradeBook()

    trade = make_trade("A")

    book.add(trade)

    assert trade in list(book.values())


def test_items():
    book = TradeBook()

    trade = make_trade("A")

    book.add(trade)

    items = dict(book.items())

    assert items["A"] is trade


def test_clear():
    book = TradeBook()

    book.add(make_trade("A"))
    book.add(make_trade("B"))

    assert len(book) == 2

    book.clear()

    assert len(book) == 0


def test_contains():
    book = TradeBook()

    trade = make_trade("A")

    book.add(trade)

    assert "A" in book
    assert "UNKNOWN" not in book


def test_iteration():
    book = TradeBook()

    a = make_trade("A")
    b = make_trade("B")

    book.add(a)
    book.add(b)

    trades = list(book)

    assert len(trades) == 2
    assert a in trades
    assert b in trades


def test_repr():
    book = TradeBook()

    assert "TradeBook" in repr(book)