#!/usr/bin/python3
"""Dördbucaqlını təyin edən modul."""


class Rectangle:
    """Dördbucaqlını (Rectangle) təmsil edən klas.

    Attributes:
        number_of_instances (int): Yaradılmış aktiv obyektlərin sayı.
        print_symbol (any): Vizual təmsil üçün istifadə olunan simvol.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Yeni bir Rectangle yaradılır.

        Args:
            width (int): Dördbucaqlının eni.
            height (int): Dördbucaqlının hündürlüyü.
        """
        type(self).number_of_instances += 1
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

    def area(self):
        """Dördbucaqlının sahəsini qaytarır."""
        return self.__width * self.__height

    def perimeter(self):
        """Dördbucaqlının perimetrini qaytarır."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Dördbucaqlının print_symbol ilə vizual təmsilini qaytarır."""
        if self.__width == 0 or self.__height == 0:
            return ""

        rect_str = []
        for i in range(self.__height):
            # print_symbol-u string-ə çevirərək width qədər təkrarlayırıq
            rect_str.append(str(self.print_symbol) * self.__width)
        return "\n".join(rect_str)

    def __repr__(self):
        """Obyektin 'eval()' ilə yenidən yaradıla bilən string təmsilini qaytarır."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Obyekt silindikdə mesaj çap edir və sayğacı azaldır."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
