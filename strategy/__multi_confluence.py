from strategy.base_strategy import BaseStrategy

from signals.signal_result import SignalResult
from signals.signal_types import SignalType


class MultiConfluenceStrategy(BaseStrategy):

    def initialize(self):

        print("Multi Confluence Strategy Loaded")

    def generate_signal(self, row):

        # BUY

        if (
            row["ema_5"] > row["ema_21"]
            and row["rsi_14"] > 50
            and row["macd"] > row["macd_signal"]
        ):

            return SignalResult(
                signal=SignalType.BUY,
                price=row["close"],
                stop_loss=row["psar"],
                reason="EMA+RSI+MACD Bullish"
            )

        # SELL

        if (
            row["ema_5"] < row["ema_21"]
            and row["rsi_14"] < 50
            and row["macd"] < row["macd_signal"]
        ):

            return SignalResult(
                signal=SignalType.SELL,
                price=row["close"],
                stop_loss=row["psar"],
                reason="EMA+RSI+MACD Bearish"
            )

        return SignalResult(
            signal=SignalType.HOLD,
            price=row["close"],
            reason="No Setup"
        )

    def manage_position(self):

        pass

    def exit_logic(self):

        pass