from data.data_loader import DataLoader
from data.data_validator import DataValidator


class DataManager:

    @staticmethod
    def get_data(file_path):

        df = DataLoader.load_csv(file_path)

        DataValidator.validate(df)

        return df