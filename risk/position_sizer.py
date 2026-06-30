from __future__ import annotations

from decimal import Decimal


class PositionSizer:

    def fixed_quantity(
        self,
        quantity: int,
    ) -> int:

        if quantity <= 0:
            raise ValueError(
                "Quantity must be positive."
            )

        return quantity

    def cash_fraction(
        self,
        *,
        cash: Decimal,
        price: Decimal,
        fraction: Decimal,
    ) -> int:

        cash = Decimal(cash)
        price = Decimal(price)
        fraction = Decimal(fraction)

        if cash <= 0:
            raise ValueError(
                "Cash must be positive."
            )

        if price <= 0:
            raise ValueError(
                "Price must be positive."
            )

        if fraction <= 0 or fraction > 1:
            raise ValueError(
                "Fraction must be between 0 and 1."
            )

        allocation = cash * fraction

        return int(
            allocation // price
        )