from __future__ import annotations

from decimal import Decimal

from broker.order import Order
from risk.risk_rule import RiskRule


class RiskManager:

    def __init__(
        self,
        rule: RiskRule,
    ) -> None:
        self.rule = rule

    def validate_order(
        self,
        order: Order,
        price: Decimal,
        current_position_value: Decimal = Decimal("0"),
    ) -> bool:

        price = Decimal(price)
        current_position_value = Decimal(current_position_value)

        if price <= 0:
            raise ValueError(
                "Price must be positive."
            )

        order_value = (
            Decimal(order.quantity)
            * price
        )

        if order_value > self.rule.max_order_value:
            raise ValueError(
                "Order value exceeds max order value."
            )

        if (
            current_position_value + order_value
            > self.rule.max_position_value
        ):
            raise ValueError(
                "Position value exceeds max position value."
            )

        return True