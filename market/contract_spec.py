from market.instrument_master import (
    INSTRUMENTS
)

from market.lot_size_manager import (
    LotSizeManager
)


class ContractSpec:

    @staticmethod
    def get(
        instrument,
        trade_date
    ):

        instrument_data = (
            INSTRUMENTS[instrument]
        )

        lot_size = (
            LotSizeManager.get_lot_size(
                instrument,
                trade_date
            )
        )

        return {

            **instrument_data,

            "symbol": instrument,

            "lot_size": lot_size
        }