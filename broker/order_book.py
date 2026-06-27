from __future__ import annotations

from typing import Dict, Iterator, List

from broker.enums import OrderStatus
from broker.exceptions import (
    DuplicateOrderError,
    OrderNotFoundError,
)
from broker.order import Order


class OrderBook:
    """
    In-memory repository of broker orders.

    Responsible only for storing orders and tracking
    their lifecycle state.
    """

    def __init__(self) -> None:

        self._orders: Dict[str, Order] = {}

    # ---------------------------------------------------------
    # CRUD
    # ---------------------------------------------------------

    def add(self, order: Order) -> None:

        if order.order_id in self._orders:
            raise DuplicateOrderError(
                f"Order '{order.order_id}' already exists."
            )

        self._orders[order.order_id] = order

    def get(self, order_id: str) -> Order:

        try:
            return self._orders[order_id]

        except KeyError as exc:

            raise OrderNotFoundError(
                f"Order '{order_id}' not found."
            ) from exc

    def remove(self, order_id: str) -> Order:

        try:
            return self._orders.pop(order_id)

        except KeyError as exc:

            raise OrderNotFoundError(
                f"Order '{order_id}' not found."
            ) from exc

    def clear(self) -> None:

        self._orders.clear()

    # ---------------------------------------------------------
    # State Transitions
    # ---------------------------------------------------------

    def mark_partial(self, order_id: str) -> None:

        self.get(order_id).status = OrderStatus.PARTIALLY_FILLED

    def mark_filled(self, order_id: str) -> None:

        self.get(order_id).status = OrderStatus.FILLED

    def mark_cancelled(self, order_id: str) -> None:

        self.get(order_id).status = OrderStatus.CANCELLED

    def mark_rejected(self, order_id: str) -> None:

        self.get(order_id).status = OrderStatus.REJECTED

    # ---------------------------------------------------------
    # Queries
    # ---------------------------------------------------------

    def has_order(self, order_id: str) -> bool:

        return order_id in self._orders

    def all_orders(self) -> List[Order]:

        return list(self._orders.values())

    def orders_for_symbol(
        self,
        symbol: str,
    ) -> List[Order]:

        return [
            order
            for order in self._orders.values()
            if order.symbol == symbol
        ]

    def open_orders(self) -> list[Order]:

        return [
            order
            for order in self._orders.values()
            if order.status in (
                OrderStatus.PENDING,
                OrderStatus.OPEN,
                OrderStatus.PARTIALLY_FILLED,
            )
        ]

    def completed_orders(self) -> List[Order]:

        return [
            order
            for order in self._orders.values()
            if order.status in (
                OrderStatus.FILLED,
                OrderStatus.CANCELLED,
                OrderStatus.REJECTED,
            )
        ]

    def filled_orders(self) -> List[Order]:

        return [
            order
            for order in self._orders.values()
            if order.status == OrderStatus.FILLED
        ]

    def cancelled_orders(self) -> List[Order]:

        return [
            order
            for order in self._orders.values()
            if order.status == OrderStatus.CANCELLED
        ]

    def rejected_orders(self) -> List[Order]:

        return [
            order
            for order in self._orders.values()
            if order.status == OrderStatus.REJECTED
        ]

    def pending_orders(self) -> List[Order]:

        return [
            order
            for order in self._orders.values()
            if order.status == OrderStatus.PENDING
        ]

    @property
    def order_count(self) -> int:

        return len(self._orders)


    @property
    def open_count(self) -> int:

        return len(self.open_orders())

    @property
    def completed_count(self) -> int:

        return len(self.completed_orders())

    def first(self) -> Order | None:

        return next(
            iter(self._orders.values()),
            None,
        )

    def last(self) -> Order | None:

        if not self._orders:
            return None

        return next(
            reversed(self._orders.values())
        )

    # ---------------------------------------------------------
    # Container Protocol
    # ---------------------------------------------------------

    def __contains__(self, order_id: str) -> bool:

        return order_id in self._orders

    def __len__(self) -> int:

        return len(self._orders)

    def __iter__(self) -> Iterator[Order]:

        return iter(self._orders.values())

    def __repr__(self) -> str:

        return (
            f"{self.__class__.__name__}("
            f"orders={len(self)}, "
            f"open={self.open_count}, "
            f"completed={self.completed_count})"
        )