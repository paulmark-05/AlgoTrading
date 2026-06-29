from __future__ import annotations

from decimal import Decimal

from strategy.base_strategy import BaseStrategy
from strategy.context import StrategyContext
from strategy.signal import Signal, SignalSide


class NoOpStrategy(BaseStrategy):
    """
    Reference strategy for integration testing.

    Always returns HOLD.
    """

    def __init__(
        self,
        symbol: str,
        name: str = "NoOpStrategy",
    ) -> None:
        super().__init__(
            name=name,
            symbol=symbol,
        )

    def generate_signal(
        self,
        context: StrategyContext,
    ) -> Signal:

        self.validate_context(context)

        return Signal(
            symbol=self.symbol,
            side=SignalSide.HOLD,
            strength=Decimal("0"),
            reason="No operation strategy.",
        )