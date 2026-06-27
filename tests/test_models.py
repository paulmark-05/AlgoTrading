from datetime import datetime

from models import Candle

candle = Candle(
    timestamp=datetime.now(),
    symbol="NIFTY",
    timeframe="5m",
    open=100,
    high=105,
    low=99,
    close=104,
    volume=1000
)

print(candle)