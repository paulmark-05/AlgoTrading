from __future__ import annotations

import pandas as pd

from indicators.manager import IndicatorManager
from strategy.context import StrategyContext
from strategy.manager import StrategyManager
from strategy.signal import Signal


class StrategyEngine:

    def __init__(
        self,
        strategy_manager: StrategyManager,
        indicator_manager: IndicatorManager | None = None,
    ) -> None:

        self.strategy_manager = strategy_manager
        self.indicator_manager = (
            indicator_manager or IndicatorManager()
        )

    def run(
        self,
        strategy_name: str,
        symbol: str,
        data: pd.DataFrame,
    ) -> Signal:

        indicators = self.indicator_manager.calculate(data)

        context = StrategyContext(
            symbol=symbol,
            data=data,
            indicators=indicators,
        )

        return self.strategy_manager.evaluate(
            strategy_name,
            context,
        )