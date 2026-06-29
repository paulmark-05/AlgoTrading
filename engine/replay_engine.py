from __future__ import annotations

import pandas as pd

from engine.event import MarketEvent
from engine.event_bus import EventBus


class ReplayEngine:

    def __init__(
        self,
        event_bus: EventBus,
    ) -> None:
        self.event_bus = event_bus

    def replay(
        self,
        *,
        symbol: str,
        data: pd.DataFrame,
    ) -> None:

        if data.empty:
            raise ValueError(
                "Replay data cannot be empty."
            )

        for index in range(len(data)):

            event_data = data.iloc[: index + 1].copy()

            event = MarketEvent(
                symbol=symbol,
                data=event_data,
            )

            self.event_bus.publish(event)