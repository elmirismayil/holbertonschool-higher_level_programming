#!/usr/bin/python3
"""Bu modul kvadratı təyin edən Square class-ından ibarətdir."""


class Square:
    """Kvadratı təmsil edən class."""

    def __init__(self, size=0):
        """Kvadratı müəyyən bir ölçü ilə başladır.

        Args:
            size (int): Kvadratın tərəfinin ölçüsü (default 0).

        Raises:
            TypeError: Əgər size integer (tam ədəd) deyilsə.
            ValueError: Əgər size 0-dan kiçikdirsə.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
