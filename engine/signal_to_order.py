from __future__ import annotations

from broker.enums import OrderSide, OrderType
from broker.order import Order
from strategy.signal import Signal, SignalSide


class SignalToOrder:

    def convert(
        self,
        signal: Signal,
        quantity: int,
        order_type: OrderType = OrderType.MARKET,
    ) -> Order | None:

        if signal.is_hold:
            return None

        if quantity <= 0:
            raise ValueError(
                "Order quantity must be positive."
            )

        if signal.side == SignalSide.BUY:
            side = OrderSide.BUY

        elif signal.side == SignalSide.SELL:
            side = OrderSide.SELL

        else:
            return None

        return Order(
            symbol=signal.symbol,
            side=side,
            quantity=quantity,
            order_type=order_type,
            price=signal.price
            if order_type == OrderType.LIMIT
            else None,
        )