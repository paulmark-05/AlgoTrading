from decimal import Decimal

import pytest

from risk.risk_rule import RiskRule


def test_risk_rule_creation():

    rule = RiskRule(
        max_position_value=Decimal("50000"),
        max_order_value=Decimal("10000"),
    )

    assert rule.max_position_value == Decimal("50000")
    assert rule.max_order_value == Decimal("10000")


def test_invalid_max_position_value():

    with pytest.raises(ValueError):
        RiskRule(
            max_position_value=Decimal("0"),
            max_order_value=Decimal("10000"),
        )


def test_invalid_max_order_value():

    with pytest.raises(ValueError):
        RiskRule(
            max_position_value=Decimal("50000"),
            max_order_value=Decimal("0"),
        )


def test_risk_rule_is_immutable():

    rule = RiskRule(
        max_position_value=Decimal("50000"),
        max_order_value=Decimal("10000"),
    )

    with pytest.raises(Exception):
        rule.max_order_value = Decimal("1")