from decimal import Decimal

from analytics.risk_reward import RiskRewardCalculator
from analytics.trade_ledger import ClosedTrade
from analytics.trade_summary import TradeSummary


def trade(pnl):

    return ClosedTrade(
        symbol="NIFTY",
        quantity=10,
        entry_price=Decimal("100"),
        exit_price=Decimal("110"),
        gross_pnl=Decimal(pnl),
        commission=Decimal("0"),
        net_pnl=Decimal(pnl),
    )


def test_empty_risk_reward():

    summary = TradeSummary([])

    calc = RiskRewardCalculator(summary)

    assert calc.calculate() == Decimal("0")


def test_risk_reward():

    summary = TradeSummary(
        [
            trade("100"),
            trade("50"),
            trade("-50"),
        ]
    )

    calc = RiskRewardCalculator(summary)

    assert calc.calculate() == Decimal("1.5")