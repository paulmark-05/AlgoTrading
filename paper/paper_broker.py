from storage.repositories.position_repository import (
PositionRepository
)

from storage.repositories.trade_repository import (
TradeRepository
)

class PaperBroker:

    @staticmethod
    def buy(

        strategy_name,

        instrument,

        quantity,

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
                "BUY",

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

    @staticmethod
    def close_position(

        position_id,

        position,

        exit_price,

        exit_time,

        result

    ):

        pnl_points = (

            exit_price

            -

            position["entry_price"]

        )

        pnl_amount = (

            pnl_points

            *

            position["quantity"]

        )

        trade = {

            "strategy_name":
                position["strategy_name"],

            "instrument":
                position["instrument"],

            "quantity":
                position["quantity"],

            "signal":
                position["signal"],

            "entry_price":
                position["entry_price"],

            "exit_price":
                exit_price,

            "stop_loss":
                position["stop_loss"],

            "target_price":
                position["target_price"],

            "pnl_points":
                pnl_points,

            "pnl_amount":
                pnl_amount,

            "result":
                result,

            "entry_time":
                position["entry_time"],

            "exit_time":
                exit_time
        }

        TradeRepository.save(
            trade
        )

        PositionRepository.close_position(
            position_id
        )

        return trade

