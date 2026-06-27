from __future__ import annotations

from collections import defaultdict
from typing import Callable
from typing import Type


class EventBus:

    def __init__(self):

        self._subscribers = defaultdict(list)

    def subscribe(
        self,
        event_type: Type,
        callback: Callable,
    ) -> None:

        self._subscribers[event_type].append(callback)

    def unsubscribe(
        self,
        event_type: Type,
        callback: Callable,
    ) -> None:

        if callback in self._subscribers[event_type]:
            self._subscribers[event_type].remove(callback)

    def publish(self, event):

        handlers = self._subscribers.get(type(event), [])

        for handler in handlers:
            handler(event)

    def clear(self):

        self._subscribers.clear()