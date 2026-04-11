#!/usr/bin/python3
"""Dördbucaqlını təyin edən modul."""


class Rectangle:
    """Dördbucaqlını (Rectangle) təmsil edən klas."""

    def __init__(self, width=0, height=0):
        """Yeni bir Rectangle yaradılır.

        Args:
            width (int): Dördbucaqlının eni.
            height (int): Dördbucaqlının hündürlüyü.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Eni (width) əldə etmək üçün getter."""
        return self.__width

    @width.setter
    def width(self, value):
        """Eni (width) təyin etmək üçün setter."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Hündürlüyü (height) əldə etmək üçün getter."""
        return self.__height

    @height.setter
    def height(self, value):
        """Hündürlüyü (height) təyin etmək üçün setter."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
