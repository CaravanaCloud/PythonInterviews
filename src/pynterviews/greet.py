"""Send greetings."""

import arrow

import sys


def greet():
    """Greet a location."""
    return f"Hello hello."


def cli(args=None):
    """Process command line arguments."""
    if not args:
        args = sys.argv[1:]
    print(greet())
