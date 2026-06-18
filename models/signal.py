from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Signal:
    strategy_name: str
    instrument: str

    signal: str              # BUY / SELL / EXIT / HOLD

    entry_price: Optional[float] = None
    stop_loss: Optional[float] = None
    target_price: Optional[float] = None

    quantity: int = 0

    timestamp: Optional[datetime] = None

    reason: str = ""