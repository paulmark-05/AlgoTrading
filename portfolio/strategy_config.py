class StrategyConfig:

    STRATEGIES = {

        "nifty_5m_bazooka": {

            "instrument": "NIFTY",

            "capital_per_lot": 50000,

            "allocated_lots": 1,

            "enabled": True
        }
    }

    @classmethod
    def get(cls, strategy_name):

        return cls.STRATEGIES[
            strategy_name
        ]