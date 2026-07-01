from datetime import datetime, timedelta
from decimal import Decimal

from analytics.trade_duration import (
    TradeDurationCalculator,
)
from analytics.trade_ledger import ClosedTrade


def trade(minutes):

    start = datetime(
        2025,
        1,
        1,
        10,
        0,
    )

    end = start + timedelta(
        minutes=minutes
    )

    return ClosedTrade(
        symbol="NIFTY",
        quantity=10,
        entry_price=Decimal("100"),
        exit_price=Decimal("110"),
        gross_pnl=Decimal("100"),
        commission=Decimal("0"),
        net_pnl=Decimal("100"),
        entry_time=start,
        exit_time=end,
    )


def test_average_duration():

    calc = TradeDurationCalculator(
        [
            trade(5),
            trade(15),
            trade(10),
        ]
    )

    assert calc.average_duration() == timedelta(
        minutes=10
    )


def test_longest_duration():

    calc = TradeDurationCalculator(
        [
            trade(5),
            trade(20),
            trade(10),
        ]
    )

    assert calc.longest_duration() == timedelta(
        minutes=20
    )


def test_shortest_duration():

    calc = TradeDurationCalculator(
        [
            trade(5),
            trade(20),
            trade(10),
        ]
    )

    assert calc.shortest_duration() == timedelta(
        minutes=5
    )


def test_empty_duration():

    calc = TradeDurationCalculator([])

    assert calc.average_duration() == timedelta()
    assert calc.longest_duration() == timedelta()
    assert calc.shortest_duration() == timedelta()