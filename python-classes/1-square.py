#!/usr/bin/python3
"""
This module defines a Square class.
"""


class Square:
    """
    Defines a square by its size.
    """

    def __init__(self, size):
        """
        Initializes the square with a private size attribute.

        Args:
            size (int): The width/height of the square.
        """
        self.__size = size
