#!/usr/bin/python3
"""Kvadratı təyin edən modul."""


class Square:
    """Kvadratı təmsil edən class."""

    def __init__(self, size=0):
        """Kvadratı müəyyən bir ölçü ilə başladır.

        Args:
            size (int): Kvadratın tərəfinin ölçüsü (default 0).
        """
        self.size = size

    @property
    def size(self):
        """Ölçünü geri qaytarır (Getter)."""
        return self.__size

    @size.setter
    def size(self, value):
        """Ölçünü təyin edir və yoxlamadan keçirir (Setter).

        Args:
            value (int): Yeni ölçü dəyəri.

        Raises:
            TypeError: Əgər value integer deyilsə.
            ValueError: Əgər value 0-dan kiçikdirsə.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Kvadratın cari sahəsini qaytarır.

        Returns:
            Kvadratın sahəsi.
        """
        return self.__size * self.__size
