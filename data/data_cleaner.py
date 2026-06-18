import pandas as pd


class DataCleaner:

    @staticmethod
    def clean(df):

        df["date"] = pd.to_datetime(
            df["date"],
            format="%d-%m-%Y %H:%M"
        )

        df = df.sort_values(
            by="date"
        )

        df = df.drop_duplicates()

        df = df.reset_index(
            drop=True
        )

        return df