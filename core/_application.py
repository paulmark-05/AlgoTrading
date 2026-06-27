from portfolio.strategy_registry import (
    StrategyRegistry
)

from portfolio.capital_allocator import (
    CapitalAllocator
)


class Application:

    def __init__(self):

        self.strategies = []

    def initialize(self):

        required_capital = (

            CapitalAllocator.required_capital()
        )

        print()

        print(
            "=" * 60
        )

        print(
            "TRADING PLATFORM STARTING"
        )

        print(
            "Required Capital:",
            required_capital
        )

        print(
            "=" * 60
        )

        self.strategies = (

            StrategyRegistry
            .get_active_strategies()
        )

        print()

        print(
            "Loaded Strategies:"
        )

        for strategy in self.strategies:

            print(
                strategy["name"]
            )

    def run(self):

        print()

        print(
            "Platform Running..."
        )