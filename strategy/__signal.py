from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Signal:
    symbol: str
    timestamp: datetime

    action: str          # BUY / SELL / EXIT / HOLD

    price: float

    quantity: int = 0

    strength: float = 0.0

    strategy: str = ""

    reason: str = ""

    stop_loss: Optional[float] = None

    target: Optional[float] = None

    metadata: Optional[dict] = None