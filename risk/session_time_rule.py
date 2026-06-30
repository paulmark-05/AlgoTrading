from __future__ import annotations

from datetime import time

from broker.order import Order
from risk.base_risk_rule import BaseRiskRule


class SessionTimeRule(BaseRiskRule):

    def __init__(
        self,
        entry_start: time = time(9, 25),
        entry_end: time = time(15, 10),
    ) -> None:

        if entry_start >= entry_end:
            raise ValueError(
                "Entry start must be before entry end."
            )

        self.entry_start = entry_start
        self.entry_end = entry_end

    def validate(
        self,
        order: Order,
        **context,
    ) -> None:

        current_time = context.get(
            "current_time"
        )

        if current_time is None:
            raise ValueError(
                "current_time is required for session validation."
            )

        if current_time < self.entry_start:
            raise ValueError(
                "Entry not allowed before session start."
            )

        if current_time > self.entry_end:
            raise ValueError(
                "Entry not allowed after session end."
            )