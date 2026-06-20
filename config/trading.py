"""
Trading defaults.

These values are broker-independent.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class TradingSettings:

    BROKERAGE_PERCENT: float = 0.03

    SLIPPAGE_PERCENT: float = 0.01

    RISK_PER_TRADE: float = 1.0

    MAX_OPEN_POSITIONS: int = 1

    CONTRACT_SIZE: int = 1

    ALLOW_SHORT_SELL: bool = False

    PAPER_TRADING: bool = True


TRADING = TradingSettings()