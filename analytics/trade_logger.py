import os
import pandas as pd


class TradeLogger:

    REPORT_FOLDER = "reports"

    @staticmethod
    def save_trades(trades):

        if len(trades) == 0:
            return

        os.makedirs(
            TradeLogger.REPORT_FOLDER,
            exist_ok=True
        )

        df = pd.DataFrame(trades)

        file_path = os.path.join(
            TradeLogger.REPORT_FOLDER,
            "trades.csv"
        )

        df.to_csv(
            file_path,
            index=False
        )

        print(
            f"\nTrade report saved -> {file_path}"
        )