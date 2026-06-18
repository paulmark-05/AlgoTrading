class ExecutionService:

    def __init__(

        self,

        broker
    ):

        self.broker = broker

    def execute(

        self,

        trade_intent
    ):

        return self.broker.place_order(
            trade_intent
        )