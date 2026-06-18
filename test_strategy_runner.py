from runner.strategy_runner import (
StrategyRunner
)

runner = StrategyRunner()

runner.register(
    "Bazooka",
    object()

)

print(
    runner.get_strategies()
)
