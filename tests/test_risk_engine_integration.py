from datetime import time
from decimal import Decimal

import pandas as pd
import pytest

from broker.paper_broker import PaperBroker
from engine.strategy_engine import StrategyEngine
from engine.trading_engine import TradingEngine
from risk.max_drawdown_rule import MaxDrawdownRule
from risk.risk_engine import RiskEngine
from risk.session_time_rule import SessionTimeRule
from strategy.base_strategy import BaseStrategy
from strategy.context import StrategyContext
from strategy.manager import StrategyManager
from strategy.signal import Signal, SignalSide


class AlwaysBuyStrategy(BaseStrategy):

    def generate_signal(
        self,
        context: StrategyContext,
    ) -> Signal:

        return Signal(
            symbol=context.symbol,
            side=SignalSide.BUY,
        )


def sample_df():

    return pd.DataFrame(
        {
            "datetime": ["2025-01-01"],
            "open": [100],
            "high": [110],
            "low": [90],
            "close": [105],
            "volume": [1000],
        }
    )


def make_trading_engine(risk_engine=None):

    manager = StrategyManager()

    manager.add(
        AlwaysBuyStrategy(
            name="AlwaysBuy",
            symbol="NIFTY",
        )
    )

    strategy_engine = StrategyEngine(
        strategy_manager=manager,
    )

    broker = PaperBroker(
        initial_cash=Decimal("100000")
    )

    engine = TradingEngine(
        strategy_engine=strategy_engine,
        broker=broker,
        risk_manager=risk_engine,
    )

    return engine, broker


def test_risk_engine_allows_valid_order():

    risk_engine = RiskEngine()

    risk_engine.add_rule(
        MaxDrawdownRule(
            max_drawdown=Decimal("5000")
        )
    )

    risk_engine.add_rule(
        SessionTimeRule()
    )

    engine, broker = make_trading_engine(
        risk_engine
    )

    engine.run_once(
        strategy_name="AlwaysBuy",
        symbol="NIFTY",
        data=sample_df(),
        quantity=10,
        market_price=Decimal("100"),
        risk_context={
            "current_drawdown": Decimal("1000"),
            "current_time": time(10, 0),
        },
    )

    assert len(broker.order_book) == 1
    assert len(broker.trade_book) == 1
    assert broker.has_position("NIFTY")


def test_risk_engine_blocks_max_drawdown_breach():

    risk_engine = RiskEngine()

    risk_engine.add_rule(
        MaxDrawdownRule(
            max_drawdown=Decimal("5000")
        )
    )

    risk_engine.add_rule(
        SessionTimeRule()
    )

    engine, broker = make_trading_engine(
        risk_engine
    )

    with pytest.raises(ValueError):
        engine.run_once(
            strategy_name="AlwaysBuy",
            symbol="NIFTY",
            data=sample_df(),
            quantity=10,
            market_price=Decimal("100"),
            risk_context={
                "current_drawdown": Decimal("5000"),
                "current_time": time(10, 0),
            },
        )

    assert len(broker.order_book) == 0
    assert len(broker.trade_book) == 0


def test_risk_engine_blocks_outside_session():

    risk_engine = RiskEngine()

    risk_engine.add_rule(
        MaxDrawdownRule(
            max_drawdown=Decimal("5000")
        )
    )

    risk_engine.add_rule(
        SessionTimeRule()
    )

    engine, broker = make_trading_engine(
        risk_engine
    )

    with pytest.raises(ValueError):
        engine.run_once(
            strategy_name="AlwaysBuy",
            symbol="NIFTY",
            data=sample_df(),
            quantity=10,
            market_price=Decimal("100"),
            risk_context={
                "current_drawdown": Decimal("1000"),
                "current_time": time(15, 11),
            },
        )

    assert len(broker.order_book) == 0
    assert len(broker.trade_book) == 0