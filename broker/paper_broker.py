from broker.base_broker import BaseBroker


class PaperBroker(BaseBroker):

    def connect(self):
        print("Paper Broker Connected")

    def place_order(
        self,
        symbol,
        side,
        quantity,
        order_type="MARKET"
    ):
        print(
            f"[PAPER] {side} {quantity} {symbol}"
        )