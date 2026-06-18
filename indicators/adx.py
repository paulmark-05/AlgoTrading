import pandas_ta as ta


class ADXIndicator:

    @staticmethod
    def calculate(df, length=14):

        adx = ta.adx(
            high=df["high"],
            low=df["low"],
            close=df["close"],
            length=length
        )

        df[f"adx_{length}"] = adx[f"ADX_{length}"]

        return df