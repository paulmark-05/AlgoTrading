from portfolio.strategy_registry import (
    StrategyRegistry
)


class StrategyService:

    @staticmethod
    def load_active():

        return (
            StrategyRegistry
            .get_active_strategies()
        )