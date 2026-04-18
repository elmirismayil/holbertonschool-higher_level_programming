#!/usr/bin/env python3

class SwimMixin:
    """Mixin to add swimming behavior."""
    def swim(self):
        print("The creature swims!")

class FlyMixin:
    """Mixin to add flying behavior."""
    def fly(self):
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    """
    Dragon class that composes behaviors from SwimMixin and FlyMixin.
    This demonstrates the use of mixins for modular functionality.
    """
    def roar(self):
        print("The dragon roars!")
