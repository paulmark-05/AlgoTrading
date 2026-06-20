"""
Application-wide settings.

Only global application configuration belongs here.
Do NOT place strategy-specific parameters in this file.
"""

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class AppSettings:
    APP_NAME: str = "Trading Platform"

    DEFAULT_SYMBOL: str = "NIFTY"

    DEFAULT_TIMEFRAME: str = "5m"

    TIMEZONE: str = "Asia/Kolkata"

    INITIAL_CAPITAL: float = 100000.0

    PROJECT_ROOT: Path = Path(__file__).resolve().parent.parent

    DATA_DIR: Path = PROJECT_ROOT / "data"

    LOG_DIR: Path = PROJECT_ROOT / "logs"

    REPORT_DIR: Path = PROJECT_ROOT / "reports"


SETTINGS = AppSettings()