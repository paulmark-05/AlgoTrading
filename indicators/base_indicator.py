"""
base_indicator.py

Abstract base class for all technical indicators.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

import pandas as pd


class BaseIndicator(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Indicator name.
        """
        ...

    @abstractmethod
    def calculate(
        self,
        data: pd.DataFrame,
    ) -> pd.Series:
        """
        Calculate indicator values.
        """
        ...