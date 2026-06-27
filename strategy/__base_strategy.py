from abc import ABC, abstractmethod


class BaseStrategy(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def initialize(self):
        """Load configuration."""
        pass

    @abstractmethod
    def generate_signal(
        self,
        symbol,
        market_data,
        indicators
    ):
        """Return a Signal or None."""
        pass

    @abstractmethod
    def on_order_filled(self, order):
        pass

    @abstractmethod
    def on_position_closed(self, position):
        pass