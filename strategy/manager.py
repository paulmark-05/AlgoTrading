from __future__ import annotations

from strategy.base_strategy import BaseStrategy
from strategy.context import StrategyContext
from strategy.signal import Signal


class StrategyManager:

    def __init__(self) -> None:
        self._strategies: dict[str, BaseStrategy] = {}

    def add(
        self,
        strategy: BaseStrategy,
    ) -> None:
        self._strategies[strategy.name] = strategy

    def get(
        self,
        name: str,
    ) -> BaseStrategy | None:
        return self._strategies.get(name)

    def has(
        self,
        name: str,
    ) -> bool:
        return name in self._strategies

    def all(self) -> list[BaseStrategy]:
        return list(self._strategies.values())

    def evaluate(
        self,
        name: str,
        context: StrategyContext,
    ) -> Signal:

        strategy = self.get(name)

        if strategy is None:
            raise ValueError(
                f"Strategy not found: {name}"
            )

        return strategy.generate_signal(context)

    def clear(self) -> None:
        self._strategies.clear()

    def __len__(self) -> int:
        return len(self._strategies)

    def __contains__(
        self,
        name: str,
    ) -> bool:
        return name in self._strategies