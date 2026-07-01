from __future__ import annotations

import json
from dataclasses import asdict
from datetime import time
from decimal import Decimal
from pathlib import Path

from config.trading_config import TradingConfig


class ConfigReporter:

    def save(
        self,
        *,
        config: TradingConfig,
        path: str | Path,
    ) -> Path:

        path = Path(path)

        path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        data = asdict(config)

        with path.open(
            "w",
            encoding="utf-8",
        ) as file:
            json.dump(
                data,
                file,
                indent=4,
                default=self._serialize,
            )

        return path

    def _serialize(
        self,
        value,
    ) -> str:

        if isinstance(value, Decimal):
            return str(value)

        if isinstance(value, time):
            return value.strftime("%H:%M")

        return str(value)