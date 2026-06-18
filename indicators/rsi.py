from config.settings import settings

import pandas_ta as ta


class RSIIndicator:

    @staticmethod
    def calculate(df, length=14):

        df = df.copy()

        source = settings.get_indicator_source()

        df[f"rsi_{length}"] = ta.rsi(
            df[source],
            length=length
        )

        return df