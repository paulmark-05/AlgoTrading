from decimal import Decimal
import pytest
import pandas as pd

from broker.paper_broker import PaperBroker
from engine.trading_engine import TradingEngine
from engine.strategy_engine import StrategyEngine
from strategy.base_strategy import BaseStrategy
from strategy.context import StrategyContext
from strategy.manager import StrategyManager
from strategy.reference.noop_strategy import NoOpStrategy
from strategy.signal import Signal, SignalSide
from risk.risk_engine import RiskEngine
from risk.max_drawdown_rule import MaxDrawdownRule

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


def test_trading_engine_hold_does_not_place_order():

    manager = StrategyManager()
    manager.add(
        NoOpStrategy(symbol="NIFTY")
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
    )

    signal = engine.run_once(
        strategy_name="NoOpStrategy",
        symbol="NIFTY",
        data=sample_df(),
        quantity=10,
        market_price=Decimal("100"),
    )

    assert signal.side == SignalSide.HOLD
    assert len(broker.order_book) == 0
    assert len(broker.trade_book) == 0


def test_trading_engine_buy_places_order():

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
    )

    signal = engine.run_once(
        strategy_name="AlwaysBuy",
        symbol="NIFTY",
        data=sample_df(),
        quantity=10,
        market_price=Decimal("100"),
    )

def test_trading_engine_risk_rejects_large_order():

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

    risk_manager = RiskEngine()

    risk_manager.add_rule(
        MaxDrawdownRule(
            max_drawdown=Decimal("1")
        )
    )

    engine = TradingEngine(
        strategy_engine=strategy_engine,
        broker=broker,
        risk_manager=risk_manager,
    )

    with pytest.raises(ValueError):
        engine.run_once(
            strategy_name="AlwaysBuy",
            symbol="NIFTY",
            data=sample_df(),
            quantity=100,
            market_price=Decimal("100"),
            risk_context={
                "current_drawdown": Decimal("1"),
            },
        )

    assert len(broker.order_book) == 0
    assert len(broker.trade_book) == 0

    # assert broker.has_position("NIFTY") is True