from __future__ import annotations

from core.component import Component


class LifecycleManager:

    def __init__(self):

        self._components: list[Component] = []

    def register(self, component: Component):

        self._components.append(component)

    def initialize(self):

        for component in self._components:
            component.initialize()

    def start(self):

        for component in self._components:
            component.start()

    def stop(self):

        for component in reversed(self._components):
            component.stop()

    def shutdown(self):

        for component in reversed(self._components):
            component.shutdown()