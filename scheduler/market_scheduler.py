import time

class MarketScheduler:


    def __init__(

        self,

        engine

    ):

        self.engine = engine

    def run_once(self):

        print(

            "Running Trading Cycle"

        )

    def run_forever(self):

        while True:

            self.run_once()

            time.sleep(
                300
            )

