from analytics.trade_logger import (
    TradeLogger
)


class ReportingService:

    @staticmethod
    def generate(trades):

        TradeLogger.save_trades(
            trades
        )