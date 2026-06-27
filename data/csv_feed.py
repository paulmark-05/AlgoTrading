from pathlib import Path

import pandas as pd


class CSVFeed:
    """
    Loads historical OHLCV data from CSV.
    """

    REQUIRED_COLUMNS = [
        "datetime",
        "open",
        "high",
        "low",
        "close",
        "volume",
    ]

    def __init__(self, csv_path):
        self.csv_path = Path(csv_path)

    def load(self) -> pd.DataFrame:

        if not self.csv_path.exists():
            raise FileNotFoundError(self.csv_path)

        df = pd.read_csv(self.csv_path)

        # Normalize column names
        df.columns = [c.strip().lower() for c in df.columns]

        # Accept common datetime column names
        datetime_columns = [
            "datetime",
            "date",
            "timestamp",
            "time",
        ]

        datetime_col = None

        for col in datetime_columns:
            if col in df.columns:
                datetime_col = col
                break

        if datetime_col is None:
            raise ValueError(
                "CSV must contain one of: datetime, date, timestamp, time"
            )

        # Rename to our internal standard
        if datetime_col != "datetime":
            df.rename(columns={datetime_col: "datetime"}, inplace=True)

        # Parse datetime
        df["datetime"] = pd.to_datetime(
            df["datetime"],
            dayfirst=True
        )

        required = [
            "datetime",
            "open",
            "high",
            "low",
            "close",
            "volume",
        ]

        missing = set(required) - set(df.columns)

        if missing:
            raise ValueError(f"Missing columns: {missing}")

        df.sort_values("datetime", inplace=True)

        df.reset_index(drop=True, inplace=True)

        return df