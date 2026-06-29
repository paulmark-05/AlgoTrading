from decimal import Decimal

from analytics.win_rate import WinRateCalculator
from broker.trade_book import TradeBook


def test_empty_win_rate():

    trade_book = TradeBook()

    calc = WinRateCalculator(
        trade_book
    )

    assert calc.calculate() == Decimal("0")