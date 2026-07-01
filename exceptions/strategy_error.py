from exceptions.trading_error import TradingError


class StrategyError(TradingError):
    """
    Raised for strategy-related failures.
    """