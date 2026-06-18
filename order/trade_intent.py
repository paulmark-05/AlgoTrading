from dataclasses import dataclass


@dataclass
class TradeIntent:

    strategy_name: str

    instrument: str

    signal: str

    lots: int

    entry_price: float

    stop_loss: float

    target_price: float

    timestamp: object