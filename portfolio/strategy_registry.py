class StrategyRegistry:

    STRATEGIES = {

        "nifty_5m_bazooka": {

            "class":
                "backtest.bazooka_backtester.BazookaBacktester",

            "enabled": True
        }
    }

    @classmethod
    def get_active_strategies(cls):

        active = []

        for strategy_name, config in cls.STRATEGIES.items():

            if config["enabled"]:

                active.append({

                    "name": strategy_name,

                    "class": config["class"]
                })

        return active