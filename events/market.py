from dataclasses import dataclass

from events.base import Event

from models.candle import Candle


@dataclass(slots=True)
class CandleEvent(Event):

    candle: Candle


@dataclass(slots=True)
class TickEvent(Event):

    symbol: str

    price: float