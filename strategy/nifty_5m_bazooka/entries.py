from strategy.nifty_5m_bazooka.filters import BazookaFilters


class BazookaEntries:

    @staticmethod
    def long_entry(df, i):

        return (

            BazookaFilters.adx_bullish(df, i)

            and

            BazookaFilters.plus_di_rising(df, i)

            and

            BazookaFilters.rsi_bullish(df, i)

            and

            BazookaFilters.rsi_rising(df, i)

            and

            BazookaFilters.sar_bullish(df, i)

            and

            BazookaFilters.ema_bullish(df, i)

            and

            BazookaFilters.macd_bullish(df, i)

            and

            BazookaFilters.macd_diff_rising(df, i)

            and

            BazookaFilters.histogram_bullish(df, i)

            and

            BazookaFilters.histogram_rising(df, i)
        )

    @staticmethod
    def short_entry(df, i):

        return (

            BazookaFilters.adx_bearish(df, i)

            and

            BazookaFilters.minus_di_rising(df, i)

            and

            BazookaFilters.rsi_bearish(df, i)

            and

            BazookaFilters.rsi_falling(df, i)

            and

            BazookaFilters.sar_bearish(df, i)

            and

            BazookaFilters.ema_bearish(df, i)

            and

            BazookaFilters.macd_bearish(df, i)

            and

            BazookaFilters.macd_diff_falling(df, i)

            and

            BazookaFilters.histogram_bearish(df, i)

            and

            BazookaFilters.histogram_falling(df, i)
        )