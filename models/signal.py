from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class Signal:

    timestamp: datetime

    symbol: str

    action: str

    confidence: float