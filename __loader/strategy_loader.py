from strategies.nifty_5m_bazooka import Nifty5MBazooka


class StrategyLoader:

    def __init__(
        self,
        runner,
        settings,
        market_data,
        broker
    ):

        self.runner = runner

        self.settings = settings

        self.market_data = market_data

        self.broker = broker

    def load_all(self):

        strategy = Nifty5MBazooka()

        self.runner.register(

            "nifty_5m_bazooka",

            strategy

        )