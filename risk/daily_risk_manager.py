from config.settings import settings


class DailyRiskManager:

    def __init__(self):

        self.reset()

    def reset(self):

        self.daily_pnl = 0

        self.trade_count = 0

        self.trading_enabled = True

    def register_trade(
        self,
        pnl_amount
    ):

        self.daily_pnl += pnl_amount

        self.trade_count += 1

        self._check_limits()

    def _check_limits(self):

        loss_limit = settings.get(
            "risk",
            "daily_loss_limit_percent"
        )

        profit_limit = settings.get(
            "risk",
            "daily_profit_lock_percent"
        )

        max_trades = settings.get(
            "risk",
            "max_trades_per_day"
        )

        capital = settings.get(
            "risk",
            "starting_capital"
        )

        daily_loss_amount = (
            capital * loss_limit / 100
        )

        daily_profit_amount = (
            capital * profit_limit / 100
        )

        if self.daily_pnl <= -daily_loss_amount:

            self.trading_enabled = False

        if self.daily_pnl >= daily_profit_amount:

            self.trading_enabled = False

        if self.trade_count >= max_trades:

            self.trading_enabled = False

    def can_trade(self):

        return self.trading_enabled

    def get_status(self):

        return {

            "daily_pnl":
                self.daily_pnl,

            "trade_count":
                self.trade_count,

            "trading_enabled":
                self.trading_enabled
        }