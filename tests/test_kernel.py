from core.component import Component
from core.kernel import ApplicationKernel


class Dummy(Component):

    def __init__(self):
        self.started = False

    def start(self):
        self.started = True


kernel = ApplicationKernel()

dummy = Dummy()

kernel.register("dummy", dummy)

kernel.start()

assert dummy.started

print("PASS")