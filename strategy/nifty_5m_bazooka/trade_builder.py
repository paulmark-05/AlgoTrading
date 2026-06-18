from signals.signal_result import SignalResult
from signals.signal_types import SignalType


class TradeBuilder:

    @staticmethod
    def build_long(row):

        entry = row["close"]

        sl = row["psar"]

        risk = entry - sl

        target = entry + (risk * 1.5)

        return SignalResult(
            SignalType.BUY,
            entry,
            sl,
            "Bazooka Long"
        ), target

    @staticmethod
    def build_short(row):

        entry = row["close"]

        sl = row["psar"]

        risk = sl - entry

        target = entry - (risk * 1.5)

        return SignalResult(
            SignalType.SELL,
            entry,
            sl,
            "Bazooka Short"
        ), target