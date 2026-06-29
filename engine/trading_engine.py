from __future__ import annotations

import pandas as pd

from broker.paper_broker import PaperBroker
from engine.signal_to_order import SignalToOrder
from engine.strategy_engine import StrategyEngine
from strategy.signal import Signal


class TradingEngine:

    def __init__(
        self,
        strategy_engine: StrategyEngine,
        broker: PaperBroker,
        signal_to_order: SignalToOrder | None = None,
    ) -> None:

        self.strategy_engine = strategy_engine
        self.broker = broker
        self.signal_to_order = (
            signal_to_order or SignalToOrder()
        )

    def run_once(
        self,
        *,
        strategy_name: str,
        symbol: str,
        data: pd.DataFrame,
        quantity: int,
        market_price,
    ) -> Signal:

        signal = self.strategy_engine.run(
            strategy_name=strategy_name,
            symbol=symbol,
            data=data,
        )

        order = self.signal_to_order.convert(
            signal,
            quantity=quantity,
        )

        if order is not None:
            self.broker.submit_order(
                order,
                market_price=market_price,
            )

        return signal