from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path


class BaseReporter(ABC):
    """
    Abstract base class for all report exporters.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Reporter name.
        """
        ...

    @abstractmethod
    def save(
        self,
        *,
        report: dict,
        path: str | Path,
    ) -> Path:
        """
        Save a report.
        """
        ...