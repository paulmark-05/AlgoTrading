from __future__ import annotations

from broker.enums import OrderSide
from broker.order import Order
from engine.order_request import OrderRequest
from strategy.signal import Signal, SignalSide


class SignalToOrder:

    def convert(
        self,
        signal: Signal,
        request: OrderRequest,
    ) -> Order | None:

        if signal.is_hold:
            return None

        if signal.symbol != request.symbol:
            raise ValueError(
                "Signal symbol does not match order request symbol."
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
            quantity=request.quantity,
            order_type=request.order_type,
            price=request.price,
        )