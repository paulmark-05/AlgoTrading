"""
Custom exceptions for the broker package.

All broker-specific exceptions inherit from BrokerError so that callers
can catch either specific exceptions or all broker exceptions.
"""


class BrokerError(Exception):
    """Base class for all broker exceptions."""


#
# Order exceptions
#

class OrderError(BrokerError):
    """Base class for order-related exceptions."""


class DuplicateOrderError(OrderError):
    """Raised when an order with the same ID already exists."""


class OrderNotFoundError(OrderError):
    """Raised when an order cannot be found."""


class InvalidOrderError(OrderError):
    """Raised when an order is invalid."""


class OrderStateError(OrderError):
    """Raised when an invalid operation is performed on an order."""


#
# Trade exceptions
#

class TradeError(BrokerError):
    """Base class for trade-related exceptions."""


class DuplicateTradeError(TradeError):
    """Raised when a trade with the same ID already exists."""


class TradeNotFoundError(TradeError):
    """Raised when a trade cannot be found."""


#
# Portfolio / Position exceptions
#

class PortfolioError(BrokerError):
    """Base class for portfolio-related exceptions."""


class PositionNotFoundError(PortfolioError):
    """Raised when a requested position does not exist."""


class InsufficientPositionError(PortfolioError):
    """Raised when attempting to sell more than the current position."""


class InsufficientCashError(PortfolioError):
    """Raised when there is insufficient cash to execute a trade."""


#
# Broker exceptions
#

class BrokerStateError(BrokerError):
    """Raised when the broker is in an invalid state for the requested operation."""