class StrategyRegistry:

    def __init__(self):

        self._strategies = {}

    def add(self, strategy):

        self._strategies[strategy.name] = strategy

    def all(self):

        return self._strategies.values()