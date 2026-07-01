from exceptions.trading_error import TradingError


class DataError(TradingError):
    """
    Raised for market data related failures.
    """