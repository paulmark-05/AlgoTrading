from abc import ABC
from abc import abstractmethod


class BaseStrategy(ABC):

    @abstractmethod
    def evaluate(

        self,

        df,

        i
    ):
        pass