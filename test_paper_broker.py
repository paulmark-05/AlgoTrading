from paper.paper_broker import (
PaperBroker
)

position = PaperBroker.buy(

    strategy_name="Bazooka",

    instrument="NIFTY",

    quantity=65,

    entry_price=24000,

    stop_loss=23950,

    target_price=24200,

    entry_time="2026-06-14 09:15"

)

print(

    "POSITION OPENED"

)

print(position)
