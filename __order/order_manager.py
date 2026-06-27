class OrderManager:

    def __init__(self):

        self.orders = []

    def submit(self, trade_intent):

        self.orders.append(
            trade_intent
        )

    def get_orders(self):

        return self.orders