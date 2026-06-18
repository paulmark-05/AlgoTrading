from core.order_manager import (
OrderManager
)

position = OrderManager.place_order(


strategy_name="Bazooka",

instrument="NIFTY",

quantity=65,

signal="BUY",

entry_price=24000,

stop_loss=23950,

target_price=24200,

entry_time="2026-06-14 09:15"


)

print(position)
