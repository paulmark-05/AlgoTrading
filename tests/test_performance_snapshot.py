from decimal import Decimal

import pytest

from analytics.performance_snapshot import PerformanceSnapshot


def make_snapshot():

    return PerformanceSnapshot(
        timestamp="2025-01-01",
        cash=Decimal("100000"),
        market_value=Decimal("5000"),
        total_value=Decimal("105000"),
        realized_pnl=Decimal("250"),
        unrealized_pnl=Decimal("150"),
        total_pnl=Decimal("400"),
    )


def test_snapshot_creation():

    snapshot = make_snapshot()

    assert snapshot.cash == Decimal("100000")
    assert snapshot.total_value == Decimal("105000")


def test_snapshot_is_immutable():

    snapshot = make_snapshot()

    with pytest.raises(Exception):
        snapshot.cash = Decimal("0")


def test_snapshot_requires_decimal():

    with pytest.raises(TypeError):

        PerformanceSnapshot(
            timestamp="2025-01-01",
            cash=100000,
            market_value=Decimal("0"),
            total_value=Decimal("100000"),
            realized_pnl=Decimal("0"),
            unrealized_pnl=Decimal("0"),
            total_pnl=Decimal("0"),
        )