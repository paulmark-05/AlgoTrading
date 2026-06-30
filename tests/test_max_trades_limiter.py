import pytest

from risk.max_trades_limiter import MaxTradesLimiter


def test_max_trades_limiter_creation():

    limiter = MaxTradesLimiter(
        max_trades=3
    )

    assert limiter.max_trades == 3


def test_invalid_max_trades():

    with pytest.raises(ValueError):
        MaxTradesLimiter(
            max_trades=0
        )


def test_trade_count_within_limit():

    limiter = MaxTradesLimiter(
        max_trades=3
    )

    assert limiter.validate(
        trade_count=2
    ) is True


def test_trade_count_at_limit_rejected():

    limiter = MaxTradesLimiter(
        max_trades=3
    )

    with pytest.raises(ValueError):
        limiter.validate(
            trade_count=3
        )