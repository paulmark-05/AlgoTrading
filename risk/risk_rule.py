from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True, slots=True)
class RiskRule:
    max_position_value: Decimal
    max_order_value: Decimal

    def __post_init__(self) -> None:

        if self.max_position_value <= 0:
            raise ValueError(
                "Max position value must be positive."
            )

        if self.max_order_value <= 0:
            raise ValueError(
                "Max order value must be positive."
            )