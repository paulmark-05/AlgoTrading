class TradingEngine:

    def __init__(

        self,

        strategy,

        broker,

        portfolio
    ):

        self.strategy = strategy

        self.broker = broker

        self.portfolio = portfolio

    def on_candle(

        self,

        df,

        i
    ):

        signal = self.strategy.evaluate(
            df,
            i
        )

        if signal is None:

            return

        position = self.broker.place_order(
            signal
        )

        self.portfolio.add_position(
            position
        )