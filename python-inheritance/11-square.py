#!/usr/bin/python3
"""Square modulu"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Rectangle-dan miras alan Square klassı"""

    def __init__(self, size):
        """Yeni Square yaradır və size-ı validasiya edir"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Kvadratın sahəsini qaytarır"""
        return self.__size ** 2

    def __str__(self):
        """Kvadratın str() təsvirini qaytarır"""
        return "[Square] {}/{}".format(self.__size, self.__size)
