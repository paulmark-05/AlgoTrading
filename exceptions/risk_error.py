from exceptions.trading_error import TradingError


class RiskError(TradingError):
    """
    Raised when risk validation fails.
    """