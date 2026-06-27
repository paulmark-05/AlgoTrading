import pandas as pd
from pathlib import Path


class TradeLogger:

    FILE_PATH = "logs/trades.csv"

    @classmethod
    def log_trade(cls, trade):

        Path("logs").mkdir(
            exist_ok=True
        )

        df = pd.DataFrame([trade])

        file_exists = Path(
            cls.FILE_PATH
        ).exists()

        df.to_csv(
            cls.FILE_PATH,
            mode="a",
            header=not file_exists,
            index=False
        )