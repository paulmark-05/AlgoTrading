from indicators.sma import SMA
from indicators.ema import EMA
from indicators.rsi import RSI
from indicators.macd import MACD

from indicators.atr import ATR
from indicators.adx import ADX
from indicators.dmi import DMI
from indicators.cci import CCI
from indicators.sar import ParabolicSAR
from indicators.supertrend import SuperTrend
from indicators.vwap import VWAP


class IndicatorManager:

    def __init__(self):

        self.indicators = {}

        self.register("sma20", SMA(20))
        self.register("sma50", SMA(50))

        self.register("ema20", EMA(20))
        self.register("ema50", EMA(50))

        self.register("rsi14", RSI(14))

        self.register("macd", MACD())

        self.register("atr14", ATR())

        self.register("adx14", ADX())

        self.register("dmi14", DMI())

        self.register("cci20", CCI())

        self.register("sar", ParabolicSAR())

        self.register("supertrend", SuperTrend())

        self.register("vwap", VWAP())

    def register(self, name, indicator):
        self.indicators[name] = indicator

    def calculate_all(self, data):

        results = {}

        for name, indicator in self.indicators.items():
            results[name] = indicator.calculate(data)

        return results