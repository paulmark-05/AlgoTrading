from storage.repositories.position_repository import (
PositionRepository
)

position = {


"strategy_name": "Bazooka",

"instrument": "NIFTY",

"quantity": 65,

"signal": "BUY",

"entry_price": 24000,

"stop_loss": 23950,

"target_price": 24200,

"entry_time": "2026-06-14 09:15",

"status": "OPEN"


}

PositionRepository.save(
position
)

print(
"Position Saved"
)

print(
PositionRepository.get_open_positions()
)
