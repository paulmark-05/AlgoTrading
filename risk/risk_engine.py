from __future__ import annotations

from broker.order import Order

from risk.base_risk_rule import BaseRiskRule


class RiskEngine:
    """
    Executes multiple risk rules.
    """

    def __init__(self) -> None:

        self._rules: list[BaseRiskRule] = []

    def add_rule(
        self,
        rule: BaseRiskRule,
    ) -> None:

        self._rules.append(rule)

    def validate(
        self,
        order: Order,
        **context,
    ) -> bool:

        for rule in self._rules:
            rule.validate(
                order,
                **context,
            )

        return True

    def clear(self) -> None:

        self._rules.clear()

    def __len__(self) -> int:

        return len(self._rules)