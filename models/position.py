from dataclasses import dataclass


@dataclass
class Position:

    symbol: str

    quantity: int

    average_price: float

    unrealized_pnl: float = 0.0

    realized_pnl: float = 0.0