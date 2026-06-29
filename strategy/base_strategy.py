"""
base_strategy.py

Abstract strategy interface.

A strategy receives StrategyContext and produces a Signal.

Strategies never interact with brokers directly.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

import pandas as pd

from strategy.context import StrategyContext
from strategy.signal import Signal


class BaseStrategy(ABC):
    """
    Base class for all trading strategies.
    """

    def __init__(
        self,
        name: str,
        symbol: str,
    ) -> None:

        name = name.strip()
        symbol = symbol.upper().strip()

        if not name:
            raise ValueError(
                "Strategy name cannot be empty."
            )

        if not symbol:
            raise ValueError(
                "Strategy symbol cannot be empty."
            )

        self._name = name
        self._symbol = symbol

    @property
    def name(self) -> str:
        return self._name

    @property
    def symbol(self) -> str:
        return self._symbol

    @abstractmethod
    def generate_signal(
        self,
        context: StrategyContext,
    ) -> Signal:
        """
        Generate one trading signal from strategy context.
        """
        ...

    def validate_data(
        self,
        data: pd.DataFrame,
    ) -> None:

        required = {
            "datetime",
            "open",
            "high",
            "low",
            "close",
            "volume",
        }

        missing = required - set(data.columns)

        if missing:
            raise ValueError(
                f"Missing columns: {sorted(missing)}"
            )

        if data.empty:
            raise ValueError(
                "Market data is empty."
            )

    def validate_context(
        self,
        context: StrategyContext,
    ) -> None:

        if context.symbol != self.symbol:
            raise ValueError(
                "Context symbol does not match strategy symbol."
            )

        self.validate_data(context.data)

    def __repr__(self) -> str:

        return (
            "BaseStrategy("
            f"name={self.name}, "
            f"symbol={self.symbol})"
        )