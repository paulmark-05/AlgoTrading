class PerformanceReport:

    @staticmethod
    def generate(trades):

        total = len(trades)

        if total == 0:

            return {}

        wins = len(
            [
                t
                for t in trades
                if t["pnl_points"] > 0
            ]
        )

        losses = len(
            [
                t
                for t in trades
                if t["pnl_points"] < 0
            ]
        )

        gross_profit = sum(
            t["pnl_points"]
            for t in trades
            if t["pnl_points"] > 0
        )

        gross_loss = abs(
            sum(
                t["pnl_points"]
                for t in trades
                if t["pnl_points"] < 0
            )
        )

        profit_factor = (
            gross_profit / gross_loss
            if gross_loss > 0
            else 0
        )

        avg_win = (
            gross_profit / wins
            if wins > 0
            else 0
        )

        avg_loss = (
            gross_loss / losses
            if losses > 0
            else 0
        )

        rr_ratio = (
            avg_win / avg_loss
            if avg_loss > 0
            else 0
        )

        expectancy = (

            (
                wins / total
            ) * avg_win

            -

            (
                losses / total
            ) * avg_loss
        )

        return {

            "total_trades":
                total,

            "wins":
                wins,

            "losses":
                losses,

            "win_rate":
                round(
                    wins * 100 / total,
                    2
                ),

            "gross_profit":
                round(
                    gross_profit,
                    2
                ),

            "gross_loss":
                round(
                    gross_loss,
                    2
                ),

            "profit_factor":
                round(
                    profit_factor,
                    2
                ),

            "avg_win":
                round(
                    avg_win,
                    2
                ),

            "avg_loss":
                round(
                    avg_loss,
                    2
                ),

            "rr_ratio":
                round(
                    rr_ratio,
                    2
                ),

            "expectancy":
                round(
                    expectancy,
                    2
                )
        }