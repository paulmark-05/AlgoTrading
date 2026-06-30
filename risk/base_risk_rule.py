from __future__ import annotations

from abc import ABC, abstractmethod

from broker.order import Order


class BaseRiskRule(ABC):
    """
    Base class for all risk rules.
    """

    @abstractmethod
    def validate(
        self,
        order: Order,
        **context,
    ) -> None:
        """
        Raise ValueError if validation fails.
        """
        ...