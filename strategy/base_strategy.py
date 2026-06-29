"""
base_strategy.py

Abstract strategy interface.

A strategy receives market data and produces a Signal.

Strategies never interact with brokers directly.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

import pandas as pd

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
    generate_signal(
        context: StrategyContext
    ) -> Signal
        """
        Generate one trading signal from market data.
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

    def __repr__(self) -> str:

        return (
            "BaseStrategy("
            f"name={self.name}, "
            f"symbol={self.symbol})"
        )