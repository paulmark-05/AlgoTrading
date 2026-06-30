from datetime import time

import pytest

from broker.enums import OrderSide, OrderType
from broker.order import Order
from risk.session_time_rule import SessionTimeRule


def make_order():

    return Order(
        symbol="NIFTY",
        side=OrderSide.BUY,
        quantity=1,
        order_type=OrderType.MARKET,
    )


def test_session_time_rule_defaults():

    rule = SessionTimeRule()

    assert rule.entry_start == time(9, 25)
    assert rule.entry_end == time(15, 10)


def test_invalid_session_time():

    with pytest.raises(ValueError):
        SessionTimeRule(
            entry_start=time(15, 10),
            entry_end=time(9, 25),
        )


def test_entry_allowed_inside_session():

    rule = SessionTimeRule()

    assert rule.validate(
        make_order(),
        current_time=time(10, 0),
    ) is None


def test_entry_rejected_before_session():

    rule = SessionTimeRule()

    with pytest.raises(ValueError):
        rule.validate(
            make_order(),
            current_time=time(9, 20),
        )


def test_entry_rejected_after_session():

    rule = SessionTimeRule()

    with pytest.raises(ValueError):
        rule.validate(
            make_order(),
            current_time=time(15, 11),
        )


def test_missing_current_time_rejected():

    rule = SessionTimeRule()

    with pytest.raises(ValueError):
        rule.validate(
            make_order()
        )