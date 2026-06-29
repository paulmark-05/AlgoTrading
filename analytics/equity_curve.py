from __future__ import annotations

from decimal import Decimal

import pandas as pd


class EquityCurve:

    def __init__(self) -> None:
        self._records: list[dict] = []

    def add(
        self,
        *,
        timestamp,
        equity: Decimal | float | int,
    ) -> None:

        equity = Decimal(equity)

        self._records.append(
            {
                "timestamp": timestamp,
                "equity": equity,
            }
        )

    def to_frame(self) -> pd.DataFrame:

        return pd.DataFrame(self._records)

    def clear(self) -> None:
        self._records.clear()

    def __len__(self) -> int:
        return len(self._records)