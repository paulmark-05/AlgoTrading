from dataclasses import dataclass
from datetime import datetime


@dataclass
class Trade:

    entry_time: datetime

    exit_time: datetime | None

    entry_price: float

    exit_price: float | None

    quantity: int

    pnl: float = 0.0