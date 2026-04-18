#!/usr/bin/python3
"""Defines a class BaseGeometry"""


class BaseGeometry:
    """A class with a public instance method area"""

    def area(self):
        """Raises an Exception because area is not implemented"""
        raise Exception("area() is not implemented")
