from decimal import Decimal

import pytest

from risk.position_sizer import PositionSizer


def test_fixed_quantity():

    sizer = PositionSizer()

    assert sizer.fixed_quantity(10) == 10


def test_fixed_quantity_invalid():

    sizer = PositionSizer()

    with pytest.raises(ValueError):
        sizer.fixed_quantity(0)


def test_cash_fraction():

    sizer = PositionSizer()

    qty = sizer.cash_fraction(
        cash=Decimal("100000"),
        price=Decimal("1000"),
        fraction=Decimal("0.25"),
    )

    assert qty == 25


def test_cash_fraction_invalid_cash():

    sizer = PositionSizer()

    with pytest.raises(ValueError):
        sizer.cash_fraction(
            cash=Decimal("0"),
            price=Decimal("100"),
            fraction=Decimal("0.5"),
        )


def test_cash_fraction_invalid_price():

    sizer = PositionSizer()

    with pytest.raises(ValueError):
        sizer.cash_fraction(
            cash=Decimal("1000"),
            price=Decimal("0"),
            fraction=Decimal("0.5"),
        )


def test_cash_fraction_invalid_fraction():

    sizer = PositionSizer()

    with pytest.raises(ValueError):
        sizer.cash_fraction(
            cash=Decimal("1000"),
            price=Decimal("100"),
            fraction=Decimal("1.5"),
        )