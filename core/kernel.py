from __future__ import annotations

from core.event_bus import EventBus
from core.lifecycle import LifecycleManager
from core.registry import ServiceRegistry


class ApplicationKernel:

    """
    Central runtime kernel.
    """

    def __init__(self):

        self.registry = ServiceRegistry()

        self.lifecycle = LifecycleManager()

        self.event_bus = EventBus()

    def register(self, name: str, service):

        self.registry.register(name, service)

        if hasattr(service, "initialize"):
            self.lifecycle.register(service)

    def resolve(self, name: str):

        return self.registry.resolve(name)

    def initialize(self):

        self.lifecycle.initialize()

    def start(self):

        self.lifecycle.start()

    def stop(self):

        self.lifecycle.stop()

    def shutdown(self):

        self.lifecycle.shutdown()