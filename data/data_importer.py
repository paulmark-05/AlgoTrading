import pandas as pd


class DataImporter:

    @staticmethod
    def import_csv(file_path):

        df = pd.read_csv(file_path)

        return df