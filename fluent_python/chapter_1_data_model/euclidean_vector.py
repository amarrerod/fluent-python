"""
    euclidean_vector.py: A simple class demonstrating some special methods

    It is simplistic for didactic reasons. It lacks proper error handling, 
    especially in the ``__add__`` and  ```__mul__`` methods.
"""

import math


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        # !r se aplica repr() al valor antes de formatearlo
        return f"Vector({self.x!r}, {self.y!r})"

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(self.x or self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y
