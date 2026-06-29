from decimal import Decimal

from analytics.trade_ledger import TradeLedger
from broker.enums import OrderSide
from broker.trade import Trade
from broker.trade_book import TradeBook


def make_trade(
    trade_id,
    side,
    quantity,
    price,
    commission="0",
):

    return Trade(
        trade_id=trade_id,
        order_id=f"ORD-{trade_id}",
        symbol="NIFTY",
        side=side,
        quantity=quantity,
        price=Decimal(price),
        commission=Decimal(commission),
    )


def test_empty_trade_ledger():

    book = TradeBook()
    ledger = TradeLedger(book)

    assert ledger.closed_trades() == []


def test_single_closed_trade_profit():

    book = TradeBook()

    book.add(
        make_trade(
            "B1",
            OrderSide.BUY,
            10,
            "100",
        )
    )

    book.add(
        make_trade(
            "S1",
            OrderSide.SELL,
            10,
            "120",
        )
    )

    ledger = TradeLedger(book)

    closed = ledger.closed_trades()

    assert len(closed) == 1
    assert closed[0].quantity == 10
    assert closed[0].entry_price == Decimal("100")
    assert closed[0].exit_price == Decimal("120")
    assert closed[0].gross_pnl == Decimal("200")
    assert closed[0].net_pnl == Decimal("200")
    assert closed[0].is_winner is True


def test_single_closed_trade_loss():

    book = TradeBook()

    book.add(
        make_trade(
            "B1",
            OrderSide.BUY,
            10,
            "100",
        )
    )

    book.add(
        make_trade(
            "S1",
            OrderSide.SELL,
            10,
            "90",
        )
    )

    ledger = TradeLedger(book)

    closed = ledger.closed_trades()

    assert len(closed) == 1
    assert closed[0].gross_pnl == Decimal("-100")
    assert closed[0].net_pnl == Decimal("-100")
    assert closed[0].is_loser is True


def test_partial_exit_creates_closed_trade():

    book = TradeBook()

    book.add(
        make_trade(
            "B1",
            OrderSide.BUY,
            10,
            "100",
        )
    )

    book.add(
        make_trade(
            "S1",
            OrderSide.SELL,
            4,
            "120",
        )
    )

    ledger = TradeLedger(book)

    closed = ledger.closed_trades()

    assert len(closed) == 1
    assert closed[0].quantity == 4
    assert closed[0].gross_pnl == Decimal("80")


def test_multiple_entries_average_price():

    book = TradeBook()

    book.add(
        make_trade(
            "B1",
            OrderSide.BUY,
            10,
            "100",
        )
    )

    book.add(
        make_trade(
            "B2",
            OrderSide.BUY,
            10,
            "120",
        )
    )

    book.add(
        make_trade(
            "S1",
            OrderSide.SELL,
            20,
            "130",
        )
    )

    ledger = TradeLedger(book)

    closed = ledger.closed_trades()

    assert len(closed) == 1
    assert closed[0].quantity == 20
    assert closed[0].entry_price == Decimal("110")
    assert closed[0].gross_pnl == Decimal("400")


def test_commission_reduces_net_pnl():

    book = TradeBook()

    book.add(
        make_trade(
            "B1",
            OrderSide.BUY,
            10,
            "100",
            commission="5",
        )
    )

    book.add(
        make_trade(
            "S1",
            OrderSide.SELL,
            10,
            "120",
            commission="5",
        )
    )

    ledger = TradeLedger(book)

    closed = ledger.closed_trades()

    assert closed[0].gross_pnl == Decimal("200")
    assert closed[0].commission == Decimal("10")
    assert closed[0].net_pnl == Decimal("190")