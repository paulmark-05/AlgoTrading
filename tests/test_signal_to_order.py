from decimal import Decimal

import pytest

from broker.enums import OrderSide, OrderType
from engine.order_request import OrderRequest
from engine.signal_to_order import SignalToOrder
from strategy.signal import Signal, SignalSide


def test_hold_signal_returns_none():

    converter = SignalToOrder()

    signal = Signal(
        symbol="NIFTY",
        side=SignalSide.HOLD,
    )

    request = OrderRequest(
        symbol="NIFTY",
        quantity=10,
    )

    assert converter.convert(
        signal,
        request,
    ) is None


def test_buy_signal_to_market_order():

    converter = SignalToOrder()

    signal = Signal(
        symbol="NIFTY",
        side=SignalSide.BUY,
    )

    request = OrderRequest(
        symbol="NIFTY",
        quantity=10,
    )

    order = converter.convert(
        signal,
        request,
    )

    assert order.symbol == "NIFTY"
    assert order.side == OrderSide.BUY
    assert order.quantity == 10
    assert order.order_type == OrderType.MARKET


def test_sell_signal_to_market_order():

    converter = SignalToOrder()

    signal = Signal(
        symbol="NIFTY",
        side=SignalSide.SELL,
    )

    request = OrderRequest(
        symbol="NIFTY",
        quantity=10,
    )

    order = converter.convert(
        signal,
        request,
    )

    assert order.side == OrderSide.SELL


def test_limit_order_uses_request_price():

    converter = SignalToOrder()

    signal = Signal(
        symbol="NIFTY",
        side=SignalSide.BUY,
    )

    request = OrderRequest(
        symbol="NIFTY",
        quantity=10,
        order_type=OrderType.LIMIT,
        price=Decimal("22500"),
    )

    order = converter.convert(
        signal,
        request,
    )

    assert order.order_type == OrderType.LIMIT
    assert order.price == Decimal("22500")


def test_symbol_mismatch_rejected():

    converter = SignalToOrder()

    signal = Signal(
        symbol="NIFTY",
        side=SignalSide.BUY,
    )

    request = OrderRequest(
        symbol="BANKNIFTY",
        quantity=10,
    )

    with pytest.raises(ValueError):
        converter.convert(
            signal,
            request,
        )