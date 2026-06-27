from dataclasses import dataclass
from datetime import datetime


@dataclass
class Order:

    order_id: str

    symbol: str

    side: str

    quantity: int

    price: float

    timestamp: datetime

    status: str