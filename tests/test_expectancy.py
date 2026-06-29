from decimal import Decimal

from analytics.expectancy import ExpectancyCalculator
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


def test_empty_expectancy():

    summary = TradeSummary([])

    calc = ExpectancyCalculator(summary)

    assert calc.calculate() == Decimal("0")


def test_expectancy():

    summary = TradeSummary(
        [
            trade("100"),
            trade("-50"),
            trade("50"),
        ]
    )

    calc = ExpectancyCalculator(summary)

    assert calc.calculate() == Decimal("33.33333333333333333333333333")