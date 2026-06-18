import pandas as pd

class DataStorage:

    @staticmethod
    def save_parquet(df, file_path):

        df.to_parquet(
            file_path,
            index=False
        )

        print(
            f"\nSaved Successfully:\n{file_path}"
        )

    @staticmethod
    def load_parquet(file_path):

        return pd.read_parquet(file_path)