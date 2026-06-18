from config.settings import settings

from indicators.ema import EMAIndicator
from indicators.rsi import RSIIndicator
from indicators.macd import MACDIndicator
from indicators.adx import ADXIndicator
from indicators.cci import CCIIndicator
from indicators.sar import SARIndicator

from indicators.dmi import DMIIndicator
from indicators.supertrend import SupertrendIndicator

class IndicatorManager:

    @staticmethod
    def calculate_all(df):

        # ------------------------
        # EMA
        # ------------------------

        ema_periods = settings.get_ema_periods()

        for period in ema_periods:

            df = EMAIndicator.calculate(
                df,
                length=period
            )

        # ------------------------
        # RSI
        # ------------------------

        df = RSIIndicator.calculate(
            df,
            length=14
        )

        # ------------------------
        # MACD
        # ------------------------

        df = MACDIndicator.calculate(df)

        # ------------------------
        # ADX
        # ------------------------

        df = ADXIndicator.calculate(
            df,
            length=14
        )

        # ------------------------
        # DMI
        # ------------------------

        df = DMIIndicator.calculate(
            df,
            length=14
        )

        # ------------------------
        # CCI
        # ------------------------

        df = CCIIndicator.calculate(
            df,
            length=20
        )

        # ------------------------
        # PSAR
        # ------------------------

        df = SARIndicator.calculate(df)


        # ------------------------
        # SUPER TREND
        # ------------------------

        df = SupertrendIndicator.calculate(
            df,
            length=10,
            multiplier=3
        )

        return df