import pandas_ta as ta


class SARIndicator:

    @staticmethod
    def calculate(df):

        sar = ta.psar(
            high=df["high"],
            low=df["low"]
        )

        psar_column = sar.columns[0]

        df["psar"] = sar[psar_column]

        return df