from decimal import Decimal

import pytest

from broker.enums import OrderSide, OrderType
from broker.order import Order
from risk.risk_manager import RiskManager
from risk.risk_rule import RiskRule


def make_order(quantity=10):

    return Order(
        symbol="NIFTY",
        side=OrderSide.BUY,
        quantity=quantity,
        order_type=OrderType.MARKET,
    )


def test_valid_order():

    rule = RiskRule(
        max_position_value=Decimal("50000"),
        max_order_value=Decimal("20000"),
    )

    manager = RiskManager(rule)

    assert manager.validate_order(
        make_order(),
        price=Decimal("1000"),
    ) is True


def test_order_value_exceeds_limit():

    rule = RiskRule(
        max_position_value=Decimal("50000"),
        max_order_value=Decimal("5000"),
    )

    manager = RiskManager(rule)

    with pytest.raises(ValueError):
        manager.validate_order(
            make_order(),
            price=Decimal("1000"),
        )


def test_position_value_exceeds_limit():

    rule = RiskRule(
        max_position_value=Decimal("12000"),
        max_order_value=Decimal("20000"),
    )

    manager = RiskManager(rule)

    with pytest.raises(ValueError):
        manager.validate_order(
            make_order(),
            price=Decimal("1000"),
            current_position_value=Decimal("3000"),
        )


def test_invalid_price():

    rule = RiskRule(
        max_position_value=Decimal("50000"),
        max_order_value=Decimal("20000"),
    )

    manager = RiskManager(rule)

    with pytest.raises(ValueError):
        manager.validate_order(
            make_order(),
            price=Decimal("0"),
        )