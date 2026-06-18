import pandas_ta as ta


class DMIIndicator:

    @staticmethod
    def calculate(df, length=14):

        dmi = ta.adx(
            high=df["high"],
            low=df["low"],
            close=df["close"],
            length=length
        )

        df[f"adx_{length}"] = dmi[f"ADX_{length}"]

        df[f"plus_di_{length}"] = dmi[f"DMP_{length}"]

        df[f"minus_di_{length}"] = dmi[f"DMN_{length}"]

        return df