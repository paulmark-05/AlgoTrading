class EquityCurve:

    @staticmethod
    def generate(trades):

        equity = []

        running_equity = 0

        peak = 0

        max_drawdown = 0

        consecutive_wins = 0
        consecutive_losses = 0

        max_consecutive_wins = 0
        max_consecutive_losses = 0

        for trade in trades:

            pnl = trade["pnl_points"]

            running_equity += pnl

            equity.append(running_equity)

            # Peak tracking

            if running_equity > peak:

                peak = running_equity

            drawdown = peak - running_equity

            if drawdown > max_drawdown:

                max_drawdown = drawdown

            # Win streak

            if pnl > 0:

                consecutive_wins += 1

                consecutive_losses = 0

            elif pnl < 0:

                consecutive_losses += 1

                consecutive_wins = 0

            max_consecutive_wins = max(
                max_consecutive_wins,
                consecutive_wins
            )

            max_consecutive_losses = max(
                max_consecutive_losses,
                consecutive_losses
            )

        return {

            "max_drawdown":
                round(
                    max_drawdown,
                    2
                ),

            "max_consecutive_wins":
                max_consecutive_wins,

            "max_consecutive_losses":
                max_consecutive_losses
        }