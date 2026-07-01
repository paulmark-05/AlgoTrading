from __future__ import annotations

import csv
from pathlib import Path

from analytics.trade_ledger import ClosedTrade


class TradeReporter:

    def save(
        self,
        *,
        trades: list[ClosedTrade],
        path: str | Path,
    ) -> Path:

        path = Path(path)

        path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with path.open(
            "w",
            newline="",
            encoding="utf-8",
        ) as file:

            writer = csv.writer(file)

            writer.writerow(
                [
                    "symbol",
                    "quantity",
                    "entry_price",
                    "exit_price",
                    "gross_pnl",
                    "commission",
                    "net_pnl",
                    "entry_time",
                    "exit_time",
                ]
            )

            for trade in trades:

                writer.writerow(
                    [
                        trade.symbol,
                        trade.quantity,
                        trade.entry_price,
                        trade.exit_price,
                        trade.gross_pnl,
                        trade.commission,
                        trade.net_pnl,
                        trade.entry_time,
                        trade.exit_time,
                    ]
                )

        return path