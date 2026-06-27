from dataclasses import dataclass

from events.base import Event


@dataclass(slots=True)
class SignalEvent(Event):

    strategy: str

    signal: str

    symbol: str


@dataclass(slots=True)
class OrderEvent(Event):

    order: dict


@dataclass(slots=True)
class FillEvent(Event):

    order_id: str

    fill_price: float