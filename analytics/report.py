from __future__ import annotations

from decimal import Decimal

from analytics.drawdown import DrawdownCalculator
from analytics.expectancy import ExpectancyCalculator
from analytics.performance_tracker import PerformanceTracker
from analytics.recovery_factor import RecoveryFactorCalculator
from analytics.returns import ReturnsCalculator
from analytics.sharpe import SharpeCalculator
from analytics.sortino import SortinoCalculator
from analytics.streaks import StreakCalculator
from analytics.trade_ledger import TradeLedger
from analytics.trade_summary import TradeSummary
from analytics.volatility import VolatilityCalculator
from broker.trade_book import TradeBook
from analytics.cagr import CAGRCalculator
from analytics.calmar import CalmarCalculator
from analytics.exposure import ExposureCalculator
from analytics.risk_reward import RiskRewardCalculator
from analytics.trade_duration import TradeDurationCalculator


class PerformanceReport:

    def __init__(
        self,
        tracker: PerformanceTracker,
        trade_book: TradeBook | None = None,
    ) -> None:

        self.tracker = tracker
        self.trade_book = trade_book

    def to_dict(self) -> dict[str, Decimal | int]:

        returns = ReturnsCalculator(self.tracker)
        drawdown = DrawdownCalculator(self.tracker)
        volatility = VolatilityCalculator(self.tracker)
        sharpe = SharpeCalculator(self.tracker)
        sortino = SortinoCalculator(self.tracker)
        recovery = RecoveryFactorCalculator(self.tracker)
        cagr = CAGRCalculator(self.tracker)
        calmar = CalmarCalculator(self.tracker)
        exposure = ExposureCalculator(self.tracker)

        result: dict[str, Decimal | int] = {
            "snapshots": len(self.tracker),
            "total_return": returns.total_return(),
            "max_drawdown": drawdown.max_drawdown(),
            "volatility": volatility.calculate(),
            "sharpe": sharpe.calculate(),
            "sortino": sortino.calculate(),
            "recovery_factor": recovery.calculate(),
            "cagr": cagr.calculate(),
            "calmar": calmar.calculate(),
            "exposure": exposure.exposure_ratio(),
        }

        if self.trade_book is not None:

            ledger = TradeLedger(self.trade_book)
            closed_trades = ledger.closed_trades()
            summary = TradeSummary(closed_trades)
            expectancy = ExpectancyCalculator(summary)
            streaks = StreakCalculator(summary)
            risk_reward = RiskRewardCalculator(summary)
            duration = TradeDurationCalculator(closed_trades)

            result.update(
                {
                    "closed_trades": summary.count(),
                    "win_rate": summary.win_rate(),
                    "net_pnl": summary.net_pnl(),
                    "profit_factor": summary.profit_factor(),
                    "expectancy": expectancy.calculate(),
                    "average_win": summary.average_win(),
                    "average_loss": summary.average_loss(),
                    "largest_win": summary.largest_win(),
                    "largest_loss": summary.largest_loss(),
                    "max_winning_streak": streaks.max_winning_streak(),
                    "max_losing_streak": streaks.max_losing_streak(),
                    "risk_reward": risk_reward.calculate(),
                    "average_duration": duration.average_duration(),
                    "longest_duration": duration.longest_duration(),
                    "shortest_duration": duration.shortest_duration(),
                }
            )

        return result