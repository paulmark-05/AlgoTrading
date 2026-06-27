from abc import ABC
from abc import abstractmethod


class BaseFeed(ABC):

    @abstractmethod
    def next_candle(self):
        pass