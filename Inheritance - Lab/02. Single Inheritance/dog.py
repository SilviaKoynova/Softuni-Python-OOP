from project.animal import Animal


class Dog(Animal):
    def bark(self):
        return f"barking..."

# test animal
import unittest

from project.animal import Animal
from project.dog import Dog