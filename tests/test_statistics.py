from decimal import Decimal

from analytics.statistics import Statistics


def test_mean():

    values = [
        Decimal("1"),
        Decimal("2"),
        Decimal("3"),
    ]

    assert Statistics.mean(values) == Decimal("2")


def test_mean_empty():

    assert Statistics.mean([]) == Decimal("0")


def test_minimum():

    values = [
        Decimal("5"),
        Decimal("2"),
        Decimal("7"),
    ]

    assert Statistics.minimum(values) == Decimal("2")


def test_maximum():

    values = [
        Decimal("5"),
        Decimal("2"),
        Decimal("7"),
    ]

    assert Statistics.maximum(values) == Decimal("7")


def test_stddev_positive():

    values = [
        Decimal("1"),
        Decimal("2"),
        Decimal("3"),
    ]

    assert Statistics.stddev(values) > Decimal("0")


def test_stddev_single_value():

    values = [Decimal("5")]

    assert Statistics.stddev(values) == Decimal("0")