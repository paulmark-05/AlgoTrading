class StrategyManager:

    def __init__(self):

        self._strategies = []

    def register(self, strategy):

        strategy.initialize()

        self._strategies.append(strategy)

    def unregister(self, strategy_name):

        self._strategies = [
            s
            for s in self._strategies
            if s.name != strategy_name
        ]

    @property
    def strategies(self):

        return self._strategies

    def generate_signals(
        self,
        symbol,
        market_data,
        indicators
    ):

        signals = []

        for strategy in self._strategies:

            signal = strategy.generate_signal(
                symbol,
                market_data,
                indicators
            )

            if signal is not None:
                signals.append(signal)

        return signals