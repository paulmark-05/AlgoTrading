from abc import ABC, abstractmethod


class BaseBroker(ABC):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def place_order(
        self,
        symbol,
        side,
        quantity,
        order_type="MARKET"
    ):
        pass