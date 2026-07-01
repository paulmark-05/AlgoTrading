from exceptions.configuration_error import ConfigurationError
from exceptions.data_error import DataError
from exceptions.risk_error import RiskError
from exceptions.strategy_error import StrategyError
from exceptions.trading_error import TradingError


def test_configuration_error_is_trading_error():

    assert issubclass(
        ConfigurationError,
        TradingError,
    )


def test_risk_error_is_trading_error():

    assert issubclass(
        RiskError,
        TradingError,
    )


def test_strategy_error_is_trading_error():

    assert issubclass(
        StrategyError,
        TradingError,
    )


def test_data_error_is_trading_error():

    assert issubclass(
        DataError,
        TradingError,
    )