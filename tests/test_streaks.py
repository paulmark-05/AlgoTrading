from decimal import Decimal

from analytics.streaks import StreakCalculator
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


def test_empty_streaks():

    summary = TradeSummary([])

    calc = StreakCalculator(summary)

    assert calc.max_winning_streak() == 0
    assert calc.max_losing_streak() == 0


def test_max_winning_streak():

    summary = TradeSummary(
        [
            trade("10"),
            trade("20"),
            trade("-5"),
            trade("30"),
            trade("40"),
            trade("50"),
        ]
    )

    calc = StreakCalculator(summary)

    assert calc.max_winning_streak() == 3


def test_max_losing_streak():

    summary = TradeSummary(
        [
            trade("10"),
            trade("-5"),
            trade("-10"),
            trade("20"),
            trade("-1"),
            trade("-2"),
            trade("-3"),
        ]
    )

    calc = StreakCalculator(summary)

    assert calc.max_losing_streak() == 3