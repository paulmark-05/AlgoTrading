import json
from datetime import time
from decimal import Decimal

from config.loader import ConfigLoader


def test_config_loader_from_json(tmp_path):

    path = tmp_path / "config.json"

    path.write_text(
        json.dumps(
            {
                "symbol": "nifty",
                "initial_cash": 100000,
                "quantity": 10,
                "max_drawdown": 5000,
                "session_start": "09:25",
                "session_end": "15:10",
            }
        )
    )

    config = ConfigLoader.from_json(path)

    assert config.symbol == "NIFTY"
    assert config.initial_cash == Decimal("100000")
    assert config.quantity == 10
    assert config.max_drawdown == Decimal("5000")
    assert config.session_start == time(9, 25)
    assert config.session_end == time(15, 10)