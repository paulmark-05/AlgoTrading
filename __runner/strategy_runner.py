class StrategyRunner:

    def __init__(self):

        self.strategies = []

    def register(

        self,

        strategy_name,

        strategy_object

    ):

        self.strategies.append(

            {

                "name":
                    strategy_name,

                "strategy":
                    strategy_object

            }

        )

    def get_strategies(self):

        return self.strategies
