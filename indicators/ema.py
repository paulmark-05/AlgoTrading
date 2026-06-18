from config.settings import settings

import pandas_ta as ta


class EMAIndicator:

    @staticmethod
    def calculate(df, length=20):

        df = df.copy()

        source = settings.get_indicator_source()

        df[f"ema_{length}"] = ta.ema(
            df[source],
            length=length
        )

        return df