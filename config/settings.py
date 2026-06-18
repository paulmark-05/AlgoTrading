import yaml

class Settings:

    def __init__(self, file_path="settings.yaml"):

        with open(file_path, "r") as file:
            self.config = yaml.safe_load(file)

    def get(self, section, key):

        return self.config[section][key]

    def get_ema_periods(self):

        return self.config["indicators"]["ema_periods"]

    def get_indicator_source(self):

        return self.config["indicators"]["source_price"]

    def get_symbol(self):

        return self.config["market"]["symbol"]

    def get_lot_size(self):

        return self.config["trading"]["lot_size"]

settings = Settings()