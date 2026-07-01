import json
from decimal import Decimal

from config.trading_config import TradingConfig
from reporting.config_reporter import ConfigReporter


def test_config_reporter_saves_file(tmp_path):

    config = TradingConfig(
        symbol="NIFTY",
        initial_cash=Decimal("100000"),
        quantity=10,
        max_drawdown=Decimal("5000"),
    )

    reporter = ConfigReporter()

    path = reporter.save(
        config=config,
        path=tmp_path / "config.json",
    )

    assert path.exists()

    data = json.loads(
        path.read_text(
            encoding="utf-8",
        )
    )

    assert data["symbol"] == "NIFTY"
    assert data["initial_cash"] == "100000"
    assert data["quantity"] == 10
    assert data["max_drawdown"] == "5000"
    assert data["session_start"] == "09:25"
    assert data["session_end"] == "15:10"
    