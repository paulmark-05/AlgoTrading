import pytest

from broker.enums import OrderSide
from broker.enums import OrderType
from broker.order import Order

from risk.base_risk_rule import BaseRiskRule
from risk.risk_engine import RiskEngine


class PassRule(BaseRiskRule):

    def validate(
        self,
        order,
        **context,
    ) -> None:
        return


class FailRule(BaseRiskRule):

    def validate(
        self,
        order,
        **context,
    ) -> None:
        raise ValueError("Rejected")


def make_order():

    return Order(
        symbol="NIFTY",
        side=OrderSide.BUY,
        quantity=1,
        order_type=OrderType.MARKET,
    )


def test_empty_engine():

    engine = RiskEngine()

    assert engine.validate(make_order()) is True


def test_pass_rule():

    engine = RiskEngine()

    engine.add_rule(PassRule())

    assert engine.validate(make_order()) is True


def test_fail_rule():

    engine = RiskEngine()

    engine.add_rule(FailRule())

    with pytest.raises(ValueError):
        engine.validate(make_order())


def test_multiple_rules():

    engine = RiskEngine()

    engine.add_rule(PassRule())
    engine.add_rule(PassRule())

    assert len(engine) == 2

    assert engine.validate(make_order())


def test_clear():

    engine = RiskEngine()

    engine.add_rule(PassRule())
    engine.add_rule(PassRule())

    engine.clear()

    assert len(engine) == 0