from decimal import Decimal

from analytics.performance_snapshot import PerformanceSnapshot
from analytics.performance_tracker import PerformanceTracker
from analytics.report import PerformanceReport
from broker.enums import OrderSide
from broker.trade import Trade
from broker.trade_book import TradeBook


def make_snapshot(value):

    return PerformanceSnapshot(
        timestamp=None,
        cash=Decimal(value),
        market_value=Decimal("0"),
        total_value=Decimal(value),
        realized_pnl=Decimal("0"),
        unrealized_pnl=Decimal("0"),
        total_pnl=Decimal("0"),
    )


def make_trade(
    trade_id,
    side,
    quantity,
    price,
):

    return Trade(
        trade_id=trade_id,
        order_id=f"ORD-{trade_id}",
        symbol="NIFTY",
        side=side,
        quantity=quantity,
        price=Decimal(price),
    )


def test_performance_report_without_trade_book():

    tracker = PerformanceTracker()

    tracker.add(make_snapshot("100"))
    tracker.add(make_snapshot("120"))
    tracker.add(make_snapshot("110"))

    report = PerformanceReport(
        tracker=tracker,
    ).to_dict()

    assert report["snapshots"] == 3
    assert report["total_return"] == Decimal("0.1")
    assert report["max_drawdown"] == Decimal("10")
    assert "closed_trades" not in report


def test_performance_report_with_trade_book():

    tracker = PerformanceTracker()

    tracker.add(make_snapshot("100"))
    tracker.add(make_snapshot("120"))
    tracker.add(make_snapshot("110"))

    trade_book = TradeBook()

    trade_book.add(
        make_trade(
            "B1",
            OrderSide.BUY,
            10,
            "100",
        )
    )

    trade_book.add(
        make_trade(
            "S1",
            OrderSide.SELL,
            10,
            "120",
        )
    )

    report = PerformanceReport(
        tracker=tracker,
        trade_book=trade_book,
    ).to_dict()

    assert report["closed_trades"] == 1
    assert report["win_rate"] == Decimal("1")
    assert report["net_pnl"] == Decimal("200")
    assert report["profit_factor"] == Decimal("0")
    assert report["expectancy"] == Decimal("200")
    assert report["max_winning_streak"] == 1
    assert report["max_losing_streak"] == 0
    assert "cagr" in report
    assert "calmar" in report
    assert "exposure" in report
    assert "risk_reward" in report
    assert "average_duration" in report
    assert "longest_duration" in report
    assert "shortest_duration" in report