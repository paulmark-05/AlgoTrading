from exceptions.trading_error import TradingError


class ConfigurationError(TradingError):
    """
    Raised for invalid configuration.
    """