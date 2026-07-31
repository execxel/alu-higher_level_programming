#!/usr/bin/python3
"""
Module: 1-my_list
Description: MyList class that inherits from list and adds a print_sorted method
"""


class MyList(list):
    """
    MyList class inheriting from list.

    This class extends the built-in list class and provides a method to print
    the list in sorted order without modifying the original list.

    Methods:
        print_sorted(): Print the list sorted in ascending order
    """

    def print_sorted(self):
        """
        Print the list sorted in ascending order.

        This method prints the sorted version of the list without modifying
        the original list.

        Returns:
            None
        """
        print(sorted(self))
