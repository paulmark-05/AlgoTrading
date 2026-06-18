from datetime import datetime


class LotSizeManager:

    LOT_SIZE_HISTORY = {

        "NIFTY": [

            {
                "effective_from": "2019-01-01",
                "lot_size": 75
            },

            {
                "effective_from": "2024-11-20",
                "lot_size": 65
            }
        ],

        "BANKNIFTY": [

            {
                "effective_from": "2019-01-01",
                "lot_size": 25
            },

            {
                "effective_from": "2024-11-20",
                "lot_size": 35
            }
        ]
    }

    @classmethod
    def get_lot_size(
        cls,
        instrument,
        trade_date
    ):

        if instrument not in cls.LOT_SIZE_HISTORY:

            raise Exception(
                f"Unknown instrument: {instrument}"
            )

        history = cls.LOT_SIZE_HISTORY[
            instrument
        ]

        applicable_size = None

        for record in history:

            effective_date = datetime.strptime(
                record["effective_from"],
                "%Y-%m-%d"
            ).date()

            if trade_date >= effective_date:

                applicable_size = (
                    record["lot_size"]
                )

        if applicable_size is None:

            raise Exception(
                f"No lot size found for "
                f"{instrument}"
            )

        return applicable_size