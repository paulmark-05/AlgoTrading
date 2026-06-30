from __future__ import annotations


class MaxTradesLimiter:

    def __init__(
        self,
        max_trades: int,
    ) -> None:

        if max_trades <= 0:
            raise ValueError(
                "Max trades must be positive."
            )

        self.max_trades = max_trades

    def validate(
        self,
        trade_count: int,
    ) -> bool:

        if trade_count >= self.max_trades:
            raise ValueError(
                "Max trades limit reached."
            )

        return True