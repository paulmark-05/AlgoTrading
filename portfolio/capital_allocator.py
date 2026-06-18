from portfolio.strategy_config import (
    StrategyConfig
)


class CapitalAllocator:

    @staticmethod
    def required_capital():

        total = 0

        for strategy_name, config in (

            StrategyConfig.STRATEGIES.items()
        ):

            if not config["enabled"]:

                continue

            total += (

                config["capital_per_lot"]

                *

                config["allocated_lots"]
            )

        return total