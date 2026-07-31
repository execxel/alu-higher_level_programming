#!/usr/bin/python3
"""Class MyList that inherits from list."""


class MyList(list):
    """A list class with a print_sorted method."""

    def print_sorted(self):
        """Print the list sorted in ascending order."""
        print(sorted(self))
