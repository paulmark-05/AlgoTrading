"""
Base component for every runtime service.

Every infrastructure service should inherit from this class so the
Application Kernel can manage its lifecycle consistently.
"""

from __future__ import annotations

from abc import ABC


class Component(ABC):
    """
    Base runtime component.

    Lifecycle:

        initialize()
            ↓
        start()
            ↓
        stop()
            ↓
        shutdown()
    """

    def initialize(self) -> None:
        """Allocate resources."""
        return None

    def start(self) -> None:
        """Start processing."""
        return None

    def stop(self) -> None:
        """Stop processing."""
        return None

    def shutdown(self) -> None:
        """Release resources."""
        return None