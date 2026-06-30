from decimal import Decimal

import pytest

from risk.daily_loss_limiter import DailyLossLimiter


def test_daily_loss_limiter_creation():

    limiter = DailyLossLimiter(
        max_daily_loss=Decimal("5000")
    )

    assert limiter.max_daily_loss == Decimal("5000")


def test_invalid_max_daily_loss():

    with pytest.raises(ValueError):
        DailyLossLimiter(
            max_daily_loss=Decimal("0")
        )


def test_daily_loss_within_limit():

    limiter = DailyLossLimiter(
        max_daily_loss=Decimal("5000")
    )

    assert limiter.validate(
        daily_pnl=Decimal("-3000")
    ) is True


def test_daily_loss_limit_breached():

    limiter = DailyLossLimiter(
        max_daily_loss=Decimal("5000")
    )

    with pytest.raises(ValueError):
        limiter.validate(
            daily_pnl=Decimal("-5000")
        )