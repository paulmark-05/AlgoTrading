from __future__ import annotations

from decimal import Decimal

from broker.order import Order
from risk.base_risk_rule import BaseRiskRule


class MaxDrawdownRule(BaseRiskRule):

    def __init__(
        self,
        max_drawdown: Decimal,
    ) -> None:

        self.max_drawdown = Decimal(max_drawdown)

        if self.max_drawdown <= 0:
            raise ValueError(
                "Max drawdown must be positive."
            )

    def validate(
        self,
        order: Order,
        **context,
    ) -> None:

        current_drawdown = Decimal(
            context.get(
                "current_drawdown",
                Decimal("0"),
            )
        )

        if current_drawdown >= self.max_drawdown:
            raise ValueError(
                "Max drawdown limit breached."
            )