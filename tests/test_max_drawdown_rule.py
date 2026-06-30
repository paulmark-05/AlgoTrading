from decimal import Decimal

import pytest

from broker.enums import OrderSide, OrderType
from broker.order import Order
from risk.max_drawdown_rule import MaxDrawdownRule


def make_order():

    return Order(
        symbol="NIFTY",
        side=OrderSide.BUY,
        quantity=1,
        order_type=OrderType.MARKET,
    )


def test_max_drawdown_rule_creation():

    rule = MaxDrawdownRule(
        max_drawdown=Decimal("5000")
    )

    assert rule.max_drawdown == Decimal("5000")


def test_invalid_max_drawdown():

    with pytest.raises(ValueError):
        MaxDrawdownRule(
            max_drawdown=Decimal("0")
        )


def test_drawdown_within_limit():

    rule = MaxDrawdownRule(
        max_drawdown=Decimal("5000")
    )

    assert rule.validate(
        make_order(),
        current_drawdown=Decimal("3000"),
    ) is None


def test_drawdown_limit_breached():

    rule = MaxDrawdownRule(
        max_drawdown=Decimal("5000")
    )

    with pytest.raises(ValueError):
        rule.validate(
            make_order(),
            current_drawdown=Decimal("5000"),
        )