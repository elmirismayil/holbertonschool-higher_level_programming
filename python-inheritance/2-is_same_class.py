#!/usr/bin/python3
"""
Bu modulda is_same_class funksiyası yerləşir.
"""


def is_same_class(obj, a_class):
    """
    Obyektin məhz verilmiş klassın instansı olub-olmadığını yoxlayır.

    Args:
        obj: Yoxlanılacaq obyekt.
        a_class: Müqayisə ediləcək klass.

    Returns:
        True əgər obyekt tam olaraq a_class-ın instansıdırsa, əks halda False.
    """
    return type(obj) is a_class
