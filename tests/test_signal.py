"""
Tests for strategy.signal
"""

from decimal import Decimal

import pytest

from strategy.signal import Signal, SignalSide


def test_buy_signal_creation():

    signal = Signal(
        symbol="nifty",
        side=SignalSide.BUY,
        strength=Decimal("1"),
        price=Decimal("22500"),
        reason="Breakout",
    )

    assert signal.symbol == "NIFTY"
    assert signal.side == SignalSide.BUY
    assert signal.is_buy is True
    assert signal.is_sell is False
    assert signal.is_hold is False
    assert signal.price == Decimal("22500")


def test_sell_signal_creation():

    signal = Signal(
        symbol="NIFTY",
        side=SignalSide.SELL,
    )

    assert signal.is_sell is True


def test_hold_signal_creation():

    signal = Signal(
        symbol="NIFTY",
        side=SignalSide.HOLD,
    )

    assert signal.is_hold is True


def test_empty_symbol_rejected():

    with pytest.raises(ValueError):
        Signal(
            symbol="",
            side=SignalSide.BUY,
        )


def test_negative_strength_rejected():

    with pytest.raises(ValueError):
        Signal(
            symbol="NIFTY",
            side=SignalSide.BUY,
            strength=Decimal("-1"),
        )


def test_negative_price_rejected():

    with pytest.raises(ValueError):
        Signal(
            symbol="NIFTY",
            side=SignalSide.BUY,
            price=Decimal("-1"),
        )


def test_signal_is_immutable():

    signal = Signal(
        symbol="NIFTY",
        side=SignalSide.BUY,
    )

    with pytest.raises(Exception):
        signal.symbol = "BANKNIFTY"


def test_repr():

    signal = Signal(
        symbol="NIFTY",
        side=SignalSide.HOLD,
    )

    assert "Signal(" in repr(signal)