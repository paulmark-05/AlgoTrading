from __future__ import annotations

from pathlib import Path

from app.application import TradingApplication
from data.csv_feed import CSVFeed
from engine.backtest_result import BacktestResult


class BacktestRunner:

    def __init__(
        self,
        application: TradingApplication,
    ) -> None:
        self.application = application

    def run_csv(
        self,
        csv_path: str | Path,
    ) -> BacktestResult:

        feed = CSVFeed(csv_path)

        data = feed.load()

        return self.application.backtest.run(
            strategy_name="NoOpStrategy",
            symbol=self.application.config.symbol,
            data=data,
            quantity=self.application.config.quantity,
        )