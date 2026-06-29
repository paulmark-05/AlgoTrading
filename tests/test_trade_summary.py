from decimal import Decimal

from analytics.trade_ledger import ClosedTrade
from analytics.trade_summary import TradeSummary


def closed_trade(net_pnl):

    return ClosedTrade(
        symbol="NIFTY",
        quantity=10,
        entry_price=Decimal("100"),
        exit_price=Decimal("120"),
        gross_pnl=Decimal(net_pnl),
        commission=Decimal("0"),
        net_pnl=Decimal(net_pnl),
    )


def test_empty_summary():

    summary = TradeSummary([])

    assert summary.count() == 0
    assert summary.win_rate() == Decimal("0")
    assert summary.net_pnl() == Decimal("0")


def test_winners_and_losers():

    summary = TradeSummary(
        [
            closed_trade("100"),
            closed_trade("-50"),
            closed_trade("25"),
        ]
    )

    assert summary.count() == 3
    assert len(summary.winners()) == 2
    assert len(summary.losers()) == 1


def test_win_rate():

    summary = TradeSummary(
        [
            closed_trade("100"),
            closed_trade("-50"),
            closed_trade("25"),
            closed_trade("-10"),
        ]
    )

    assert summary.win_rate() == Decimal("0.5")


def test_net_pnl():

    summary = TradeSummary(
        [
            closed_trade("100"),
            closed_trade("-50"),
            closed_trade("25"),
        ]
    )

    assert summary.net_pnl() == Decimal("75")


def test_profit_factor():

    summary = TradeSummary(
        [
            closed_trade("100"),
            closed_trade("-50"),
            closed_trade("25"),
        ]
    )

    assert summary.profit_factor() == Decimal("2.5")

def test_average_win():

    summary = TradeSummary(
        [
            closed_trade("100"),
            closed_trade("50"),
            closed_trade("-40"),
        ]
    )

    assert summary.average_win() == Decimal("75")


def test_average_loss():

    summary = TradeSummary(
        [
            closed_trade("100"),
            closed_trade("-20"),
            closed_trade("-40"),
        ]
    )

    assert summary.average_loss() == Decimal("30")


def test_largest_win():

    summary = TradeSummary(
        [
            closed_trade("80"),
            closed_trade("120"),
            closed_trade("-10"),
        ]
    )

    assert summary.largest_win() == Decimal("120")


def test_largest_loss():

    summary = TradeSummary(
        [
            closed_trade("80"),
            closed_trade("-25"),
            closed_trade("-40"),
        ]
    )

    assert summary.largest_loss() == Decimal("-40")