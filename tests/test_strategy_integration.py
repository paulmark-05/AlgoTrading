from pathlib import Path

from data.csv_feed import CSVFeed
from strategy.context import StrategyContext
from strategy.manager import StrategyManager
from strategy.reference.noop_strategy import NoOpStrategy
from strategy.signal import SignalSide


def test_csvfeed_to_noop_strategy_integration():

    csv_path = Path("tests/data/sample.csv")

    feed = CSVFeed(csv_path)
    data = feed.load()

    context = StrategyContext(
        symbol="NIFTY",
        data=data,
    )

    manager = StrategyManager()

    strategy = NoOpStrategy(
        symbol="NIFTY"
    )

    manager.add(strategy)

    signal = manager.evaluate(
        "NoOpStrategy",
        context,
    )

    assert signal.symbol == "NIFTY"
    assert signal.side == SignalSide.HOLD