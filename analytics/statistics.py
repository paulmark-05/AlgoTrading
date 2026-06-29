from __future__ import annotations

from decimal import Decimal
import math


class Statistics:
    """
    Common statistical functions used by
    analytics calculators.
    """

    @staticmethod
    def mean(values: list[Decimal]) -> Decimal:

        if not values:
            return Decimal("0")

        return sum(values) / Decimal(len(values))

    @staticmethod
    def minimum(values: list[Decimal]) -> Decimal:

        if not values:
            return Decimal("0")

        return min(values)

    @staticmethod
    def maximum(values: list[Decimal]) -> Decimal:

        if not values:
            return Decimal("0")

        return max(values)

    @staticmethod
    def stddev(values: list[Decimal]) -> Decimal:

        if len(values) < 2:
            return Decimal("0")

        mean = Statistics.mean(values)

        variance = sum(
            (v - mean) ** 2
            for v in values
        ) / Decimal(len(values))

        return Decimal(str(math.sqrt(float(variance))))