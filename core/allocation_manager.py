from core.capital_manager import (
CapitalManager
)

from storage.repositories.allocation_repository import (
AllocationRepository
)

class AllocationManager:

    @staticmethod
    def allocate(

        strategy_name,

        lots

    ):

        required_capital = (

            CapitalManager.required_capital(
                lots
            )

        )

        if not CapitalManager.can_allocate(
            lots
        ):

            raise Exception(

                "Insufficient Capital"

            )

        AllocationRepository.save(

            strategy_name,

            lots,

            CapitalManager.capital_per_lot()

        )

        return {

            "strategy":
                strategy_name,

            "lots":
                lots,

            "capital":
                required_capital
        }

    @staticmethod
    def allocations():

        return (

            AllocationRepository
            .get_all()

        )

