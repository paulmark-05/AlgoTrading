from abc import ABC
from abc import abstractmethod


class BaseBroker(ABC):

    @abstractmethod
    def place_order(
        self,
        trade_intent
    ):
        pass

    @abstractmethod
    def close_position(
        self,
        position
    ):
        pass