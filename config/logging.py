"""
Logging configuration.

Logger implementation comes later.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class LoggingSettings:

    LOG_LEVEL: str = "INFO"

    ENABLE_CONSOLE: bool = True

    ENABLE_FILE: bool = True

    LOG_FILE_NAME: str = "trading_platform.log"


LOGGING = LoggingSettings()