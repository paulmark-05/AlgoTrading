from broker.paper_broker import PaperBroker
from data.market_data_service import MarketDataService
from core.portfolio import Portfolio

from strategy.strategy_manager import StrategyManager
from strategy.nifty_5m_bazooka.strategy import Nifty5MBazooka

class Application:

    def __init__(self, config):

        self.config = config or {}

        self.broker = PaperBroker()

        self.market_data = MarketDataService()

        self.portfolio = Portfolio()

    def start(self):

        print("=" * 60)
        print("TRADING PLATFORM STARTING")
        print("=" * 60)

        self.broker.connect()

        self.market_data.connect()

        print("Platform Ready")