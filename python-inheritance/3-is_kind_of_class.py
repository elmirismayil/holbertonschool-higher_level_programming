#!/usr/bin/python3
"""
Bu modulda is_kind_of_class funksiyası yerləşir.
"""


def is_kind_of_class(obj, a_class):
    """
    Obyektin verilmiş klassın instansı olub-olmadığını və ya 
    həmin klassdan törəyib-törəmədiyini yoxlayır.

    Args:
        obj: Yoxlanılacaq obyekt.
        a_class: Müqayisə ediləcək klass.

    Returns:
        True əgər obyekt a_class-ın instansıdırsa və ya mirasıdırsa, 
        əks halda False.
    """
    return isinstance(obj, a_class)
