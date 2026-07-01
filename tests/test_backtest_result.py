from decimal import Decimal

from analytics.performance_tracker import PerformanceTracker
from broker.paper_broker import PaperBroker
from engine.backtest_result import BacktestResult


def test_backtest_result_creation():

    broker = PaperBroker(
        initial_cash=Decimal("100000")
    )

    tracker = PerformanceTracker()

    result = BacktestResult(
        bars_processed=150,
        broker=broker,
        performance=tracker,
    )

    assert result.bars_processed == 150
    assert result.broker is broker
    assert result.performance is tracker


def test_backtest_result_is_immutable():

    broker = PaperBroker(
        initial_cash=Decimal("100000")
    )

    tracker = PerformanceTracker()

    result = BacktestResult(
        bars_processed=10,
        broker=broker,
        performance=tracker,
    )

    try:
        result.bars_processed = 100
        assert False
    except Exception:
        assert True

def test_backtest_result_report():

    broker = PaperBroker(
        initial_cash=Decimal("100000")
    )

    tracker = PerformanceTracker()

    result = BacktestResult(
        bars_processed=0,
        broker=broker,
        performance=tracker,
    )

    report = result.report()

    assert report["snapshots"] == 0
    assert report["closed_trades"] == 0

def test_backtest_result_report():

    broker = PaperBroker(
        initial_cash=Decimal("100000")
    )

    tracker = PerformanceTracker()

    result = BacktestResult(
        bars_processed=0,
        broker=broker,
        performance=tracker,
    )

    report = result.report()

    assert report["snapshots"] == 0
    assert report["closed_trades"] == 0