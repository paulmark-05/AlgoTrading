"""
Commission models for the broker.

Commission models are responsible for calculating the transaction cost
for a trade. The PaperBroker should delegate all commission calculations
to an instance of CommissionModel.
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class CommissionModel(ABC):
    """Abstract base class for commission models."""

    @abstractmethod
    def calculate(
        self,
        *,
        price: float,
        quantity: float,
    ) -> float:
        """
        Calculate the commission for a trade.

        Parameters
        ----------
        price
            Execution price.
        quantity
            Executed quantity.

        Returns
        -------
        float
            Commission amount.
        """
        raise NotImplementedError


class ZeroCommission(CommissionModel):
    """Commission-free trading."""

    def calculate(
        self,
        *,
        price: float,
        quantity: float,
    ) -> float:
        return 0.0


class FixedCommission(CommissionModel):
    """
    Fixed commission per executed trade.

    Example
    -------
    >>> FixedCommission(20.0)
    """

    def __init__(self, commission: float):
        if commission < 0:
            raise ValueError("Commission cannot be negative.")

        self.commission = float(commission)

    def calculate(
        self,
        *,
        price: float,
        quantity: float,
    ) -> float:
        return self.commission


class PercentageCommission(CommissionModel):
    """
    Percentage commission based on trade value.

    Example
    -------
    rate = 0.001

    0.1% commission

    Trade value = 100000

    Commission = 100
    """

    def __init__(self, rate: float):
        if rate < 0:
            raise ValueError("Commission rate cannot be negative.")

        self.rate = float(rate)

    def calculate(
        self,
        *,
        price: float,
        quantity: float,
    ) -> float:
        return price * quantity * self.rate