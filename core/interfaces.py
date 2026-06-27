from abc import ABC
from abc import abstractmethod


class IMarketDataFeed(ABC):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def subscribe(self, symbols):
        pass

    @abstractmethod
    def stream(self):
        pass


class IBroker(ABC):

    @abstractmethod
    def place_order(self, order):
        pass

    @abstractmethod
    def modify_order(self, order_id, updates):
        pass

    @abstractmethod
    def cancel_order(self, order_id):
        pass

    @abstractmethod
    def positions(self):
        pass


class IStrategy(ABC):

    @abstractmethod
    def initialize(self):
        pass

    @abstractmethod
    def on_market_event(self, event):
        pass

    @abstractmethod
    def shutdown(self):
        pass


class IRiskManager(ABC):

    @abstractmethod
    def validate(self, signal):
        pass


class IPortfolio(ABC):

    @abstractmethod
    def update(self, event):
        pass


class IExecutionEngine(ABC):

    @abstractmethod
    def execute(self, signal):
        pass