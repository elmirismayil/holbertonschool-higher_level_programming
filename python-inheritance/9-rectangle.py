#!/usr/bin/python3
"""Rectangle modulu"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """BaseGeometry-dən miras alan Rectangle klassı"""

    def __init__(self, width, height):
        """Yeni Rectangle yaradır və dəyərləri validasiya edir"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Rectangle-ın sahəsini hesablayır və qaytarır"""
        return self.__width * self.__height

    def __str__(self):
        """Rectangle-ın str() və print() təsvirini qaytarır"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
