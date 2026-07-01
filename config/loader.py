from __future__ import annotations

import json
from datetime import time
from decimal import Decimal
from pathlib import Path

from config.trading_config import TradingConfig


class ConfigLoader:

    @staticmethod
    def from_json(
        path: str | Path,
    ) -> TradingConfig:

        path = Path(path)

        with path.open(
            "r",
            encoding="utf-8",
        ) as file:
            data = json.load(file)

        return TradingConfig(
            symbol=data["symbol"],
            initial_cash=Decimal(str(data["initial_cash"])),
            quantity=int(data["quantity"]),
            max_drawdown=Decimal(str(data["max_drawdown"])),
            session_start=ConfigLoader._parse_time(
                data.get("session_start", "09:25")
            ),
            session_end=ConfigLoader._parse_time(
                data.get("session_end", "15:10")
            ),
        )

    @staticmethod
    def _parse_time(
        value: str,
    ) -> time:

        hour, minute = value.split(":")

        return time(
            int(hour),
            int(minute),
        )