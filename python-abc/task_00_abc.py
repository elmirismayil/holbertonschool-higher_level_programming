#!/usr/bin/env python3
from abc import ABC, abstractmethod

class Animal(ABC):
    """Abstract Base Class for all animals"""
    
    @abstractmethod
    def sound(self):
        """Abstract method to be implemented by subclasses"""
        pass

class Dog(Animal):
    """Subclass representing a dog"""
    
    def sound(self):
        """Returns the sound a dog makes"""
        return "Bark"

class Cat(Animal):
    """Subclass representing a cat"""
    
    def sound(self):
        """Returns the sound a cat makes"""
        return "Meow"
