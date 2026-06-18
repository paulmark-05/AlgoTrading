import os
import pandas as pd


class TradeLogger:

    FILE_PATH = "reports/trades.csv"

    @staticmethod
    def initialize():

        os.makedirs("reports", exist_ok=True)

        if not os.path.exists(
            TradeLogger.FILE_PATH
        ):

            df = pd.DataFrame(
                columns=[
                    "trade_id",
                    "instrument",
                    "signal",
                    "qty",
                    "entry_time",
                    "exit_time",
                    "entry_price",
                    "exit_price",
                    "stop_loss",
                    "target_price",
                    "pnl_points",
                    "pnl_amount",
                    "holding_minutes",
                    "result"
                ]
            )

            df.to_csv(
                TradeLogger.FILE_PATH,
                index=False
            )

    @staticmethod
    def log_trade(trade):

        TradeLogger.initialize()

        df = pd.read_csv(
            TradeLogger.FILE_PATH
        )

        trade["trade_id"] = len(df) + 1

        df = pd.concat(
            [
                df,
                pd.DataFrame([trade])
            ],
            ignore_index=True
        )

        df.to_csv(
            TradeLogger.FILE_PATH,
            index=False
        )