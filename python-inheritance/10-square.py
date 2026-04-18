#!/usr/bin/python3
"""Square modulu"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Rectangle-dan miras alan Square klassı"""

    def __init__(self, size):
        """Yeni Square yaradır"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
