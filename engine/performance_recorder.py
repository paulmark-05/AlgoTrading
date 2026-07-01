from __future__ import annotations

from analytics.performance_snapshot import PerformanceSnapshot
from analytics.performance_tracker import PerformanceTracker
from broker.paper_broker import PaperBroker


class PerformanceRecorder:

    def __init__(
        self,
        tracker: PerformanceTracker,
    ) -> None:
        self.tracker = tracker

    def record(
        self,
        *,
        timestamp,
        broker: PaperBroker,
    ) -> PerformanceSnapshot:

        snapshot = PerformanceSnapshot(
            timestamp=timestamp,
            cash=broker.cash,
            market_value=broker.market_value,
            total_value=broker.cash + broker.market_value,
            realized_pnl=broker.realized_pnl,
            unrealized_pnl=broker.unrealized_pnl,
            total_pnl=broker.total_pnl,
        )

        self.tracker.add(snapshot)

        return snapshot