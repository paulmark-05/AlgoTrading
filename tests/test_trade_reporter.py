from decimal import Decimal

from analytics.trade_ledger import ClosedTrade
from reporting.trade_reporter import TradeReporter


def test_trade_reporter_saves_file(tmp_path):

    trades = [
        ClosedTrade(
            symbol="NIFTY",
            quantity=10,
            entry_price=Decimal("100"),
            exit_price=Decimal("120"),
            gross_pnl=Decimal("200"),
            commission=Decimal("0"),
            net_pnl=Decimal("200"),
        )
    ]

    reporter = TradeReporter()

    path = reporter.save(
        trades=trades,
        path=tmp_path / "trades.csv",
    )

    assert path.exists()

    text = path.read_text(
        encoding="utf-8",
    )

    assert "symbol,quantity,entry_price,exit_price" in text
    assert "NIFTY,10,100,120,200,0,200" in text