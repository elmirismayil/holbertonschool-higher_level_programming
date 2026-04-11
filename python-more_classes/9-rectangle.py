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
        return self.width * self.height

    def perimeter(self):
        """Dördbucaqlının perimetrini qaytarır."""
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width * 2) + (self.height * 2)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """İki dördbucaqlıdan sahəsi böyük olanı qaytarır."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Yeni bir kvadrat (eni və hündürlüyü bərabər olan dördbucaqlı) qaytarır.

        Args:
            size (int): Kvadratın tərəfinin ölçüsü.
        """
        return cls(size, size)

    def __str__(self):
        """Dördbucaqlının print_symbol ilə vizual təmsilini qaytarır."""
        if self.width == 0 or self.height == 0:
            return ""

        rect_str = []
        for i in range(self.height):
            rect_str.append(str(self.print_symbol) * self.width)
        return "\n".join(rect_str)

    def __repr__(self):
        """Obyektin 'eval()' üçün rəsmi string təmsilini qaytarır."""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Obyekt silindikdə mesaj çap edir və sayğacı azaldır."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
