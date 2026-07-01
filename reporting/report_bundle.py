from __future__ import annotations

from pathlib import Path

from analytics.performance_tracker import PerformanceTracker
from analytics.trade_ledger import ClosedTrade
from config.trading_config import TradingConfig
from reporting.config_reporter import ConfigReporter
from reporting.equity_curve_reporter import EquityCurveReporter
from reporting.report_manager import ReportManager
from reporting.trade_reporter import TradeReporter


class ReportBundle:

    def __init__(
        self,
        manager: ReportManager,
    ) -> None:

        self.manager = manager

        self.equity_reporter = EquityCurveReporter()
        self.trade_reporter = TradeReporter()
        self.config_reporter = ConfigReporter()

    def export(
        self,
        *,
        report: dict,
        tracker: PerformanceTracker,
        trades: list[ClosedTrade],
        config: TradingConfig,
        output_directory: str | Path,
    ) -> list[Path]:

        output_directory = Path(output_directory)

        files = []

        files.extend(
            self.manager.export_all(
                report=report,
                output_dir=output_directory,
            )
        )

        files.append(
            self.equity_reporter.save(
                tracker=tracker,
                path=output_directory / "equity_curve.csv",
            )
        )

        files.append(
            self.trade_reporter.save(
                trades=trades,
                path=output_directory / "trades.csv",
            )
        )

        files.append(
            self.config_reporter.save(
                config=config,
                path=output_directory / "config.json",
            )
        )

        return files