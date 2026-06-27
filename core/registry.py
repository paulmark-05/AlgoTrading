"""
Simple dependency injection container.
"""

from __future__ import annotations


class ServiceRegistry:

    def __init__(self):

        self._services = {}

    def register(self, name: str, service):

        if name in self._services:
            raise KeyError(f"Service '{name}' already registered.")

        self._services[name] = service

    def resolve(self, name: str):

        if name not in self._services:
            raise KeyError(f"Service '{name}' not found.")

        return self._services[name]

    def exists(self, name: str) -> bool:

        return name in self._services

    def unregister(self, name: str):

        self._services.pop(name, None)

    def clear(self):

        self._services.clear()

    @property
    def services(self):

        return dict(self._services)