from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal

from broker.enums import OrderType


@dataclass(frozen=True, slots=True)
class OrderRequest:
    symbol: str
    quantity: int
    order_type: OrderType = OrderType.MARKET
    price: Decimal | None = None

    def __post_init__(self) -> None:

        symbol = self.symbol.upper().strip()

        if not symbol:
            raise ValueError(
                "OrderRequest symbol cannot be empty."
            )

        if self.quantity <= 0:
            raise ValueError(
                "OrderRequest quantity must be positive."
            )

        if self.price is not None:

            price = Decimal(self.price)

            if price <= 0:
                raise ValueError(
                    "OrderRequest price must be positive."
                )

            object.__setattr__(
                self,
                "price",
                price,
            )

        object.__setattr__(
            self,
            "symbol",
            symbol,
        )