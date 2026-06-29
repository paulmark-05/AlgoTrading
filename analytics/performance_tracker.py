from __future__ import annotations

from analytics.performance_snapshot import PerformanceSnapshot


class PerformanceTracker:
    """
    Stores chronological portfolio performance snapshots.
    """

    def __init__(self) -> None:

        self._snapshots: list[PerformanceSnapshot] = []

    def add(
        self,
        snapshot: PerformanceSnapshot,
    ) -> None:

        self._snapshots.append(snapshot)

    def latest(self) -> PerformanceSnapshot | None:

        if not self._snapshots:
            return None

        return self._snapshots[-1]

    def all(self) -> list[PerformanceSnapshot]:

        return self._snapshots.copy()

    def clear(self) -> None:

        self._snapshots.clear()

    def __len__(self) -> int:

        return len(self._snapshots)