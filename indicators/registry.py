"""
registry.py

Registry for technical indicators.
"""

from __future__ import annotations

from indicators.base_indicator import BaseIndicator


class IndicatorRegistry:

    def __init__(self) -> None:
        self._indicators: dict[str, BaseIndicator] = {}

    def add(
        self,
        indicator: BaseIndicator,
    ) -> None:

        self._indicators[indicator.name] = indicator

    def get(
        self,
        name: str,
    ) -> BaseIndicator | None:

        return self._indicators.get(name)

    def has(
        self,
        name: str,
    ) -> bool:

        return name in self._indicators

    def all(
        self,
    ) -> list[BaseIndicator]:

        return list(self._indicators.values())

    def clear(self) -> None:

        self._indicators.clear()

    def __len__(self) -> int:

        return len(self._indicators)

    def __contains__(
        self,
        name: str,
    ) -> bool:

        return name in self._indicators