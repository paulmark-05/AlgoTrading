class BazookaFilters:

    LOOKBACK = 3

    # ==================================
    # ADX / DMI
    # ==================================

    @staticmethod
    def adx_bullish(df, i):

        row = df.iloc[i]

        return (

            row["plus_di_14"] > 22

            and

            row["minus_di_14"] < 22
        )

    @staticmethod
    def adx_bearish(df, i):

        row = df.iloc[i]

        return (

            row["minus_di_14"] > 22

            and

            row["plus_di_14"] < 22
        )

    @staticmethod
    def plus_di_rising(df, i):

        if i < BazookaFilters.LOOKBACK:
            return False

        return (

            df.iloc[i]["plus_di_14"]

            >

            df.iloc[i - BazookaFilters.LOOKBACK]["plus_di_14"]
        )

    @staticmethod
    def minus_di_rising(df, i):

        if i < BazookaFilters.LOOKBACK:
            return False

        return (

            df.iloc[i]["minus_di_14"]

            >

            df.iloc[i - BazookaFilters.LOOKBACK]["minus_di_14"]
        )

    # ==================================
    # RSI
    # ==================================

    @staticmethod
    def rsi_bullish(df, i):

        rsi = df.iloc[i]["rsi_14"]

        return 20 < rsi < 80

    @staticmethod
    def rsi_bearish(df, i):

        rsi = df.iloc[i]["rsi_14"]

        return 20 < rsi < 80

    @staticmethod
    def rsi_rising(df, i):

        if i < BazookaFilters.LOOKBACK:
            return False

        return (

            df.iloc[i]["rsi_14"]

            >

            df.iloc[i - BazookaFilters.LOOKBACK]["rsi_14"]
        )

    @staticmethod
    def rsi_falling(df, i):

        if i < BazookaFilters.LOOKBACK:
            return False

        return (

            df.iloc[i]["rsi_14"]

            <

            df.iloc[i - BazookaFilters.LOOKBACK]["rsi_14"]
        )

    # ==================================
    # SAR
    # ==================================

    @staticmethod
    def sar_bullish(df, i):

        row = df.iloc[i]

        return row["psar"] < row["open"]

    @staticmethod
    def sar_bearish(df, i):

        row = df.iloc[i]

        return row["psar"] > row["open"]

    # ==================================
    # EMA
    # ==================================

    @staticmethod
    def ema_bullish(df, i):

        row = df.iloc[i]

        ema_diff = abs(
            row["ema_5"] - row["ema_9"]
        )

        if i < BazookaFilters.LOOKBACK:
            return False

        prev_diff = abs(

            df.iloc[
                i - BazookaFilters.LOOKBACK
            ]["ema_5"]

            -

            df.iloc[
                i - BazookaFilters.LOOKBACK
            ]["ema_9"]
        )

        return (

            row["ema_5"] > row["ema_9"]

            and

            ema_diff > prev_diff
        )

    @staticmethod
    def ema_bearish(df, i):

        row = df.iloc[i]

        ema_diff = abs(
            row["ema_5"] - row["ema_9"]
        )

        if i < BazookaFilters.LOOKBACK:
            return False

        prev_diff = abs(

            df.iloc[
                i - BazookaFilters.LOOKBACK
            ]["ema_5"]

            -

            df.iloc[
                i - BazookaFilters.LOOKBACK
            ]["ema_9"]
        )

        return (

            row["ema_5"] < row["ema_9"]

            and

            ema_diff > prev_diff
        )

    # ==================================
    # MACD
    # ==================================

    @staticmethod
    def macd_bullish(df, i):

        row = df.iloc[i]

        return (

            row["macd"]

            >

            row["macd_signal"]
        )

    @staticmethod
    def macd_bearish(df, i):

        row = df.iloc[i]

        return (

            row["macd"]

            <

            row["macd_signal"]
        )

    @staticmethod
    def macd_diff_rising(df, i):

        if i < BazookaFilters.LOOKBACK:
            return False

        current_diff = (

            df.iloc[i]["macd"]

            -

            df.iloc[i]["macd_signal"]
        )

        previous_diff = (

            df.iloc[
                i - BazookaFilters.LOOKBACK
            ]["macd"]

            -

            df.iloc[
                i - BazookaFilters.LOOKBACK
            ]["macd_signal"]
        )

        return current_diff > previous_diff

    @staticmethod
    def macd_diff_falling(df, i):

        if i < BazookaFilters.LOOKBACK:
            return False

        current_diff = (

            df.iloc[i]["macd"]

            -

            df.iloc[i]["macd_signal"]
        )

        previous_diff = (

            df.iloc[
                i - BazookaFilters.LOOKBACK
            ]["macd"]

            -

            df.iloc[
                i - BazookaFilters.LOOKBACK
            ]["macd_signal"]
        )

        return current_diff < previous_diff

    # ==================================
    # HISTOGRAM
    # ==================================

    @staticmethod
    def histogram_bullish(df, i):

        return (

            df.iloc[i]["macd_histogram"]

            > 0
        )

    @staticmethod
    def histogram_bearish(df, i):

        return (

            df.iloc[i]["macd_histogram"]

            < 0
        )

    @staticmethod
    def histogram_rising(df, i):

        if i < BazookaFilters.LOOKBACK:
            return False

        return (

            df.iloc[i]["macd_histogram"]

            >

            df.iloc[
                i - BazookaFilters.LOOKBACK
            ]["macd_histogram"]
        )

    @staticmethod
    def histogram_falling(df, i):

        if i < BazookaFilters.LOOKBACK:
            return False

        return (

            df.iloc[i]["macd_histogram"]

            <

            df.iloc[
                i - BazookaFilters.LOOKBACK
            ]["macd_histogram"]
        )