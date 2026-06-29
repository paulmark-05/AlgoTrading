"""
event_bus.py

Simple FIFO event bus.

The EventBus transports MarketEvents between
data sources and consumers.
"""

from __future__ import annotations

from collections import deque

from engine.event import MarketEvent


class EventBus:

    def __init__(self) -> None:

        self._queue = deque()

    def publish(
        self,
        event: MarketEvent,
    ) -> None:

        self._queue.append(event)

    def next(self) -> MarketEvent | None:

        if not self._queue:
            return None

        return self._queue.popleft()

    def clear(self) -> None:

        self._queue.clear()

    def empty(self) -> bool:

        return len(self._queue) == 0

    def __len__(self) -> int:

        return len(self._queue)