from core.capital_manager import (
CapitalManager
)

from storage.repositories.allocation_repository import (
AllocationRepository
)

class PortfolioManager:

    @staticmethod
    def capital_per_lot():

        return (
            CapitalManager.capital_per_lot()
        )
    @staticmethod
    def total_capital():

        return (
            CapitalManager.total_capital()
        )

    @staticmethod
    def allocated_capital():

        allocations = (
            AllocationRepository.get_all()
        )

        total = 0

        for row in allocations:

            lots = row[2]

            capital_per_lot = row[3]

            total += (

                lots

                *

                capital_per_lot

            )

        return total

    @staticmethod
    def free_capital():

        return (

            PortfolioManager.total_capital()

            -

            PortfolioManager.allocated_capital()

        )

    @staticmethod
    def utilization_percent():

        total = (
            PortfolioManager.total_capital()
        )

        if total == 0:

            return 0

        return round(

            (

                PortfolioManager.allocated_capital()

                /

                total

            )

            * 100,

            2

        )

    @staticmethod
    def summary():

        return {

            "total_capital":

                PortfolioManager
                .total_capital(),

            "allocated_capital":

                PortfolioManager
                .allocated_capital(),

            "free_capital":

                PortfolioManager
                .free_capital(),

            "utilization_percent":

                PortfolioManager
                .utilization_percent()

        }

