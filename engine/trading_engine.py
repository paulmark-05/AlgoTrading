from __future__ import annotations

from decimal import Decimal

import pandas as pd

from broker.paper_broker import PaperBroker
from engine.order_request import OrderRequest
from engine.signal_to_order import SignalToOrder
from engine.strategy_engine import StrategyEngine
from risk.risk_engine import RiskEngine
from strategy.signal import Signal


class TradingEngine:

    def __init__(
        self,
        strategy_engine: StrategyEngine,
        broker: PaperBroker,
        signal_to_order: SignalToOrder | None = None,
        risk_manager: RiskEngine | None = None,
    ) -> None:

        self.strategy_engine = strategy_engine
        self.broker = broker
        self.signal_to_order = (
            signal_to_order or SignalToOrder()
        )
        self.risk_manager = risk_manager

    def run_once(
        self,
        *,
        strategy_name: str,
        symbol: str,
        data: pd.DataFrame,
        quantity: int,
        market_price,
        risk_context: dict | None = None,
    ) -> Signal:

        market_price = Decimal(market_price)

        signal = self.strategy_engine.run(
            strategy_name=strategy_name,
            symbol=symbol,
            data=data,
        )

        request = OrderRequest(
            symbol=symbol,
            quantity=quantity,
        )

        order = self.signal_to_order.convert(
            signal,
            request,
        )

        if order is None:
            return signal

        if self.risk_manager is not None:

            context = risk_context or {}

            self.risk_manager.validate(
                order,
                price=market_price,
                **context,
            )

        self.broker.submit_order(
            order,
            market_price=market_price,
        )

        return signal