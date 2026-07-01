from datetime import time
from decimal import Decimal

import pytest

from config.trading_config import TradingConfig


def test_trading_config_creation():

    config = TradingConfig(
        symbol="nifty",
        initial_cash=Decimal("100000"),
        quantity=10,
        max_drawdown=Decimal("5000"),
    )

    assert config.symbol == "NIFTY"
    assert config.initial_cash == Decimal("100000")
    assert config.quantity == 10
    assert config.max_drawdown == Decimal("5000")
    assert config.session_start == time(9, 25)
    assert config.session_end == time(15, 10)


def test_empty_symbol_rejected():

    with pytest.raises(ValueError):
        TradingConfig(
            symbol="",
            initial_cash=Decimal("100000"),
            quantity=10,
            max_drawdown=Decimal("5000"),
        )


def test_invalid_initial_cash_rejected():

    with pytest.raises(ValueError):
        TradingConfig(
            symbol="NIFTY",
            initial_cash=Decimal("0"),
            quantity=10,
            max_drawdown=Decimal("5000"),
        )


def test_invalid_quantity_rejected():

    with pytest.raises(ValueError):
        TradingConfig(
            symbol="NIFTY",
            initial_cash=Decimal("100000"),
            quantity=0,
            max_drawdown=Decimal("5000"),
        )


def test_invalid_max_drawdown_rejected():

    with pytest.raises(ValueError):
        TradingConfig(
            symbol="NIFTY",
            initial_cash=Decimal("100000"),
            quantity=10,
            max_drawdown=Decimal("0"),
        )


def test_invalid_session_rejected():

    with pytest.raises(ValueError):
        TradingConfig(
            symbol="NIFTY",
            initial_cash=Decimal("100000"),
            quantity=10,
            max_drawdown=Decimal("5000"),
            session_start=time(15, 10),
            session_end=time(9, 25),
        )


def test_config_is_immutable():

    config = TradingConfig(
        symbol="NIFTY",
        initial_cash=Decimal("100000"),
        quantity=10,
        max_drawdown=Decimal("5000"),
    )

    with pytest.raises(Exception):
        config.quantity = 20