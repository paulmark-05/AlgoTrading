from paper.paper_broker import (
PaperBroker
)

class PaperTradingEngine:

    def __init__(self):

        self.active_positions = []

    def place_buy(

        self,

        strategy_name,

        instrument,

        quantity,

        entry_price,

        stop_loss,

        target_price,

        entry_time

    ):

        position = PaperBroker.buy(

            strategy_name=
                strategy_name,

            instrument=
                instrument,

            quantity=
                quantity,

            entry_price=
                entry_price,

            stop_loss=
                stop_loss,

            target_price=
                target_price,

            entry_time=
                entry_time

        )

        self.active_positions.append(
            position
        )

        return position

    def positions(self):

        return self.active_positions

