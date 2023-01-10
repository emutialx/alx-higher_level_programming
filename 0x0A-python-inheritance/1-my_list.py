#!/usr/bin/python3
"""
    1-my_list: this is Mylist() class
"""
class Mylist(list):
    """
        Mlist class inherited from list.
        Attributes:
        Methods:
            print_sorted - prints sorted list in ascending order
    """
    def print_sorted(self):
        """
            prints a list in ascending order
        """
        print(sorted(self))
