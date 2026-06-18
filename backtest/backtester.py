from analytics.trade_logger import TradeLogger
from analytics.performance_report import PerformanceReport
from analytics.equity_curve import EquityCurve

class Backtester:

    def __init__(self):

        self.trades = []

    def add_trade(
        self,
        signal,
        entry_price,
        exit_price,
        stop_loss,
        target_price,
        pnl,
        result,
        entry_time,
        exit_time,
        instrument="NIFTY",
        quantity=65
    ):

        self.trades.append(

            {
                "instrument": instrument,

                "quantity": quantity,

                "signal": signal,

                "entry_price": entry_price,

                "exit_price": exit_price,

                "stop_loss": stop_loss,

                "target_price": target_price,

                "pnl_points": pnl,

                "pnl_amount": pnl * quantity,

                "result": result,

                "entry_time": entry_time,

                "exit_time": exit_time
            }
        )

    def summary(self):

        total = len(self.trades)

        wins = len(
            [
                t
                for t in self.trades
                if t["result"] == "WIN"
            ]
        )

        losses = len(
            [
                t
                for t in self.trades
                if t["result"] == "LOSS"
            ]
        )

        ema_exits = len(
            [
                t
                for t in self.trades
                if t["result"] == "EMA EXIT"
            ]
        )

        macd_exits = len(
            [
                t
                for t in self.trades
                if t["result"] == "MACD EXIT"
            ]
        )

        sar_exits = len(
            [
                t
                for t in self.trades
                if t["result"] == "SAR EXIT"
            ]
        )

        time_exits = len(
            [
                t
                for t in self.trades
                if t["result"] == "TIME EXIT"
            ]
        )

        net_pnl_points = sum(
            t["pnl_points"]
            for t in self.trades
        )

        net_pnl_amount = sum(
            t["pnl_amount"]
            for t in self.trades
        )

        winning_trades = [
            t["pnl_points"]
            for t in self.trades
            if t["pnl_points"] > 0
        ]

        losing_trades = [
            t["pnl_points"]
            for t in self.trades
            if t["pnl_points"] < 0
        ]

        avg_win = (
            round(
                sum(winning_trades)
                / len(winning_trades),
                2
            )
            if winning_trades
            else 0
        )

        avg_loss = (
            round(
                sum(losing_trades)
                / len(losing_trades),
                2
            )
            if losing_trades
            else 0
        )

        TradeLogger.save_trades(
            self.trades
        )

        report = PerformanceReport.generate(
            self.trades
        )

        equity_stats = EquityCurve.generate(
            self.trades
        )

        return {

            **report,

            **equity_stats,

            "ema_exits":
            ema_exits,

            "macd_exits":
            macd_exits,

            "sar_exits":
                sar_exits,

            "time_exits":
                time_exits,

            "net_pnl_points":
                float(
                    round(
                        net_pnl_points,
                        2
                    )
                ),

            "net_pnl_amount":
                float(
                    round(
                        net_pnl_amount,
                        2
                    )
                )
        }