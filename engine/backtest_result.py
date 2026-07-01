from __future__ import annotations

from dataclasses import dataclass

from analytics.performance_tracker import PerformanceTracker
from analytics.report import PerformanceReport
from broker.paper_broker import PaperBroker


@dataclass(frozen=True, slots=True)
class BacktestResult:
    bars_processed: int
    broker: PaperBroker
    performance: PerformanceTracker

    def report(self) -> dict:
        return PerformanceReport(
            tracker=self.performance,
            trade_book=self.broker.trade_book,
        ).to_dict()