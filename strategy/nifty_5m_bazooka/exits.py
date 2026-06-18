class BazookaExits:


    @staticmethod
    def crossover(
        current_a,
        previous_a,
        current_b,
        previous_b
    ):
        return (
            previous_a <= previous_b
            and
            current_a > current_b
        )

    @staticmethod
    def crossunder(
        current_a,
        previous_a,
        current_b,
        previous_b
    ):
        return (
            previous_a >= previous_b
            and
            current_a < current_b
        )

    @staticmethod
    def target_hit_long(
        current_row,
        target_price
    ):
        return (
            current_row["high"]
            >=
            target_price
        )

    @staticmethod
    def ema_exit_long(
        current_row,
        previous_row
    ):
        
        
        return BazookaExits.crossunder(
            current_row["ema_5"],
            previous_row["ema_5"],
            current_row["ema_21"],
            previous_row["ema_21"]
        )

    @staticmethod
    def macd_exit_long(
        current_row,
        previous_row
    ):  

        return BazookaExits.crossunder(
            current_row["macd"],
            previous_row["macd"],
            current_row["macd_signal"],
            previous_row["macd_signal"]
        )

    @staticmethod
    def sar_exit_long(
        current_row,
        previous_row
    ):
        return BazookaExits.crossunder(
            current_row["close"],
            previous_row["close"],
            current_row["psar"],
            previous_row["psar"]
        )

    @staticmethod
    def target_hit_short(
        current_row,
        target_price
    ):
        return (
            current_row["low"]
            <=
            target_price
        )

    @staticmethod
    def ema_exit_short(
        current_row,
        previous_row
    ):
        return BazookaExits.crossover(
            current_row["ema_5"],
            previous_row["ema_5"],
            current_row["ema_21"],
            previous_row["ema_21"]
        )

    @staticmethod
    def macd_exit_short(
        current_row,
        previous_row
    ):
        return BazookaExits.crossover(
            current_row["macd"],
            previous_row["macd"],
            current_row["macd_signal"],
            previous_row["macd_signal"]
    )

    @staticmethod
    def sar_exit_short(
        current_row,
        previous_row
    ):
        return BazookaExits.crossover(
            current_row["close"],
            previous_row["close"],
            current_row["psar"],
            previous_row["psar"]
        )

        

