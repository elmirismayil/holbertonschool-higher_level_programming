#!/usr/bin/env python3

class Fish:
    """Parent class representing a fish."""
    
    def swim(self):
        """Standard swimming behavior."""
        print("The fish is swimming")

    def habitat(self):
        """Standard fish habitat."""
        print("The fish lives in water")

class Bird:
    """Parent class representing a bird."""
    
    def fly(self):
        """Standard flying behavior."""
        print("The bird is flying")

    def habitat(self):
        """Standard bird habitat."""
        print("The bird lives in the sky")

class FlyingFish(Fish, Bird):
    """
    FlyingFish inherits from both Fish and Bird.
    Demonstrates multiple inheritance and method overriding.
    """

    def swim(self):
        """Overrides Fish.swim()"""
        print("The flying fish is swimming!")

    def fly(self):
        """Overrides Bird.fly()"""
        print("The flying fish is soaring!")

    def habitat(self):
        """Overrides both parents' habitat methods."""
        print("The flying fish lives both in water and the sky!")
