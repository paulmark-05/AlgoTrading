"""
Bootstrap module.
"""

from app.application import Application


def run():
    app = Application(config={})
    app.start()