import pandas as pd

from indicators.indicator_manager import IndicatorManager
from position.position_manager import PositionManager
from backtest.backtester import Backtester

from strategy.nifty_5m_bazooka.entries import BazookaEntries
from strategy.nifty_5m_bazooka.trade_builder import TradeBuilder
from strategy.nifty_5m_bazooka.exits import BazookaExits
from strategy.nifty_5m_bazooka.session_filter import SessionFilter

from risk.daily_risk_manager import DailyRiskManager

from config.settings import settings


class BazookaBacktester:

    def __init__(self):

        self.position_manager = PositionManager()

        self.backtester = Backtester()

        self.risk_manager = DailyRiskManager()

        self.current_day = None

    def run(self, df):

        df = IndicatorManager.calculate_all(df)

        lot_size = settings.get(
            "trading",
            "lot_size"
        )

        for i in range(1, len(df)):

            current_row = df.iloc[i]

            previous_row = df.iloc[i - 1]

            current_date = (
                current_row["date"]
                .date()
            )

            # ==========================
            # DAILY RESET
            # ==========================

            if self.current_day is None:

                self.current_day = current_date

            elif current_date != self.current_day:

                self.current_day = current_date

                self.risk_manager.reset()

                print(
                    "\nNEW TRADING DAY:",
                    current_date
                )

            # ==========================
            # ENTRY
            # ==========================

            if not self.position_manager.has_position():

                if not self.risk_manager.can_trade():

                    continue

                if not SessionFilter.entry_allowed(
                    current_row["date"]
                ):
                    continue

                if BazookaEntries.long_entry(
                    df,
                    i
                ):

                    signal, target = (
                        TradeBuilder.build_long(
                            current_row
                        )
                    )

                    self.position_manager.open_position(
                        signal=signal.signal.value,
                        entry_price=signal.price,
                        stop_loss=signal.stop_loss,
                        target_price=target,
                        timestamp=current_row["date"]
                    )

                    print(
                        "LONG OPEN:",
                        current_row["date"]
                    )

            # ==========================
            # POSITION MANAGEMENT
            # ==========================

            else:

                position = (
                    self.position_manager
                    .get_position()
                )

                stop_loss = (
                    position["stop_loss"]
                )

                target_price = (
                    position["target_price"]
                )

                exit_price = None

                result = None

                # STOP LOSS

                if current_row["low"] <= stop_loss:

                    exit_price = stop_loss

                    result = "LOSS"

                # TARGET

                elif BazookaExits.target_hit_long(
                    current_row,
                    target_price
                ):

                    exit_price = target_price

                    result = "WIN"

                # EMA EXIT

                elif BazookaExits.ema_exit_long(
                    current_row,
                    previous_row
                ):

                    exit_price = current_row["open"]

                    result = "EMA EXIT"

                # MACD EXIT

                elif BazookaExits.macd_exit_long(
                    current_row,
                    previous_row
                ):

                    exit_price = current_row["open"]

                    result = "MACD EXIT"

                # SAR EXIT

                elif BazookaExits.sar_exit_long(
                    current_row,
                    previous_row
                ):

                    exit_price = current_row["open"]

                    result = "SAR EXIT"

                # TIME EXIT

                elif SessionFilter.force_exit(
                    current_row["date"]
                ):

                    exit_price = current_row["open"]

                    result = "TIME EXIT"

                if exit_price is not None:

                    pnl_points = (

                        exit_price

                        -

                        position["entry_price"]
                    )

                    pnl_amount = (

                        pnl_points

                        *

                        lot_size
                    )

                    self.risk_manager.register_trade(
                        pnl_amount
                    )

                    print(
                        "EXIT:",
                        result,
                        "| PNL:",
                        round(
                            pnl_amount,
                            2
                        )
                    )

                    print(
                        "RISK STATUS:",
                        self.risk_manager.get_status()
                    )

                    self.backtester.add_trade(

                        signal="BUY",

                        instrument="NIFTY",

                        quantity=lot_size,

                        entry_price=position[
                            "entry_price"
                        ],

                        exit_price=exit_price,

                        stop_loss=position[
                            "stop_loss"
                        ],

                        target_price=position[
                            "target_price"
                        ],

                        pnl=pnl_points,

                        result=result,

                        entry_time=position[
                            "entry_time"
                        ],

                        exit_time=current_row[
                            "date"
                        ]
                    )

                    self.position_manager.close_position()

        return self.backtester.summary()