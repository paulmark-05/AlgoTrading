from position.position import Position


class PaperBroker:

    def place_order(
        self,
        trade_intent
    ):

        return Position(

            strategy_name=
                trade_intent.strategy_name,

            instrument=
                trade_intent.instrument,

            signal=
                trade_intent.signal,

            quantity=
                trade_intent.lots,

            entry_price=
                trade_intent.entry_price,

            stop_loss=
                trade_intent.stop_loss,

            target_price=
                trade_intent.target_price,

            entry_time=
                trade_intent.timestamp
        )