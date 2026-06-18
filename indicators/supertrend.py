import pandas_ta as ta


class SupertrendIndicator:

    @staticmethod
    def calculate(
        df,
        length=10,
        multiplier=3
    ):

        st = ta.supertrend(
            high=df["high"],
            low=df["low"],
            close=df["close"],
            length=length,
            multiplier=multiplier
        )

        df[f"supertrend_{length}_{multiplier}"] = st.iloc[:, 0]

        df[f"supertrend_direction_{length}_{multiplier}"] = st.iloc[:, 1]

        return df