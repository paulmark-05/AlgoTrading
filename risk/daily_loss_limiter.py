from __future__ import annotations

from decimal import Decimal


class DailyLossLimiter:

    def __init__(
        self,
        max_daily_loss: Decimal,
    ) -> None:

        self.max_daily_loss = Decimal(max_daily_loss)

        if self.max_daily_loss <= 0:
            raise ValueError(
                "Max daily loss must be positive."
            )

    def validate(
        self,
        daily_pnl: Decimal,
    ) -> bool:

        daily_pnl = Decimal(daily_pnl)

        if daily_pnl <= -self.max_daily_loss:
            raise ValueError(
                "Daily loss limit breached."
            )

        return True