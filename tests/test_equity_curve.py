from decimal import Decimal

from analytics.equity_curve import EquityCurve


def test_new_equity_curve():

    curve = EquityCurve()

    assert len(curve) == 0


def test_add_equity_record():

    curve = EquityCurve()

    curve.add(
        timestamp="2025-01-01",
        equity=Decimal("100000"),
    )

    assert len(curve) == 1


def test_to_frame():

    curve = EquityCurve()

    curve.add(
        timestamp="2025-01-01",
        equity=Decimal("100000"),
    )

    df = curve.to_frame()

    assert len(df) == 1
    assert df.iloc[0]["equity"] == Decimal("100000")


def test_clear():

    curve = EquityCurve()

    curve.add(
        timestamp="2025-01-01",
        equity=Decimal("100000"),
    )

    curve.clear()

    assert len(curve) == 0