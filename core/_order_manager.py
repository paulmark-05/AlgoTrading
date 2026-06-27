from storage.repositories.position_repository import (
    PositionRepository
)


class OrderManager:

    @staticmethod
    def place_order(

        strategy_name,

        instrument,

        quantity,

        signal,

        entry_price,

        stop_loss,

        target_price,

        entry_time

    ):

        position = {

            "strategy_name":
                strategy_name,

            "instrument":
                instrument,

            "quantity":
                quantity,

            "signal":
                signal,

            "entry_price":
                entry_price,

            "stop_loss":
                stop_loss,

            "target_price":
                target_price,

            "entry_time":
                entry_time,

            "status":
                "OPEN"
        }

        PositionRepository.save(
            position
        )

        return position