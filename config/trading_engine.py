class TradingEngine:

    def __init__(self, kernel):

        self.kernel = kernel

        self.running = False

    def initialize(self):

        ...

    def start(self):

        self.running = True

        while self.running:

            ...

    def stop(self):

        self.running = False