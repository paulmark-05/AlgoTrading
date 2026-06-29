from __future__ import annotations

import pandas as pd

from indicators.base_indicator import BaseIndicator
from indicators.registry import IndicatorRegistry


class IndicatorManager:

    def __init__(self) -> None:
        self._registry = IndicatorRegistry()

    @property
    def registry(self) -> IndicatorRegistry:
        return self._registry

    def add(
        self,
        indicator: BaseIndicator,
    ) -> None:
        self._registry.add(indicator)

    def calculate(
        self,
        data: pd.DataFrame,
    ) -> dict[str, pd.Series]:

        results = {}

        for indicator in self._registry.all():
            results[indicator.name] = indicator.calculate(data)

        return results

    def clear(self) -> None:
        self._registry.clear()