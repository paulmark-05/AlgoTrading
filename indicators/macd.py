from config.settings import settings

import pandas_ta as ta


class MACDIndicator:

    @staticmethod
    def calculate(
        df,
        fast=12,
        slow=26,
        signal=9
    ):

        df = df.copy()

        source = settings.get_indicator_source()

        macd = ta.macd(
            df[source],
            fast=fast,
            slow=slow,
            signal=signal
        )

        df["macd"] = macd.iloc[:, 0]
        df["macd_histogram"] = macd.iloc[:, 1]
        df["macd_signal"] = macd.iloc[:, 2]

        return df