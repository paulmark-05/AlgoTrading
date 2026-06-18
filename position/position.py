from dataclasses import dataclass


@dataclass
class Position:

    strategy_name: str

    instrument: str

    signal: str

    quantity: int

    entry_price: float

    stop_loss: float

    target_price: float

    entry_time: object

    status: str = "OPEN"