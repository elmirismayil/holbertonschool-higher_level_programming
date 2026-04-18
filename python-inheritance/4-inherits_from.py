#!/usr/bin/python3
"""Inherits from class"""


def inherits_from(obj, a_class):
    """Checks if obj is an inherited instance of a_class"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
