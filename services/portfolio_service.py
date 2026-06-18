from portfolio.capital_allocator import (
    CapitalAllocator
)


class PortfolioService:

    @staticmethod
    def validate():

        required = (

            CapitalAllocator
            .required_capital()
        )

        return {

            "required_capital":
                required
        }