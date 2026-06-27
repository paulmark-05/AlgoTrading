from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class Event:

    timestamp: datetime

    event_type: str