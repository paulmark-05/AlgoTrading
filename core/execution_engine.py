class ExecutionEngine:

    def execute(self, signal):

        if not self.risk.validate(signal):

            return

        order = self.order_factory.create(signal)

        fill = self.broker.place_order(order)

        self.event_bus.publish(fill)