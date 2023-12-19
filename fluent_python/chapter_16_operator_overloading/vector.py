from array import array
import reprlib
import math
import operator
from functools import reduce
import itertools
from collections import abc


class Vector:
    typecode = "d"
    __match_args__ = ("x", "y", "z", "t")

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find("[") : -1]
        return f"Vector({components})"

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return bytes([ord(self.typecode)]) + bytes(self._components)

    def __add__(self, other):
        try:
            pairs = itertools.zip_longest(self, other, fillvalue=0.0)
            return Vector(a + b for a, b in pairs)
        except TypeError:
            return NotImplemented

    __radd__ = __add__

    def __mul__(self, scalar):
        try:
            factor = float(scalar)
        except TypeError:
            return NotImplemented

        return Vector(n * factor for n in self)

    __rmul__ = __mul__

    def __matmul__(self, other):
        if isinstance(other, abc.Sized) and isinstance(other, abc.Iterable):
            try:
                return sum(a * b for a, b in zip(self, other, strict=True))
            except ValueError:
                raise ValueError("@ requires vector of equal length")
        else:
            return NotImplemented

    __rmatmul__ = __matmul__

    def __eq__(self, other):
        if isinstance(other, Vector):
            return len(self) == len(other) and all(a == b for a, b in zip(self, other))
        else:
            return NotImplemented

    def __hash__(self):
        hashes = (hash(x) for x in self._components)
        return reduce(lambda a, b: a ^ b, hashes, 0)

    def __abs__(self):
        return math.hypot(*self)

    def __bool__(self):
        return bool(abs(self))

    def __len__(self):
        return len(self._components)

    def __getitem__(self, key):
        if isinstance(key, slice):
            cls = type(self)  # To facilitate subclassing
            return cls(self._components[key])
        index = operator.index(key)
        return self._components[index]

    def __getattr__(self, name):
        cls = type(self)
        try:
            pos = cls.__match_args__.index(name)
        except ValueError:
            pos = -1
        if 0 <= pos < len(self._components):
            return self._components[pos]
        msg = f"{cls.__name__!r} object has no attribute {name!r}"
        raise AttributeError(msg)

    def __setattr__(self, name, value):
        cls = type(self)
        if len(name) == 1:
            if name in cls.__match_args__:
                error = f"readonly attribute {attr_name!r}"
            elif name.islower():
                error = f"can't set attributes 'a' to 'z' in {cls_name!r}"
            else:
                error = ""
            if error:
                msg = error.format(cls_name=cls.__name__, attr_name=name)
                raise AttributeError(msg)
        super().__setattr__(name, value)

    def angle(self, n):
        r = math.hypot(*self[n:])
        a = math.atan2(r, self[n - 1])
        if (n == len(self) - 1) and (self[-1] < 0):
            return math.pi * 2 - a
        else:
            return a

    def angles(self):
        return (self.angle(n) for n in range(1, len(self)))

    def __format__(self, fmt_spec=""):
        if fmt_spec.endswith("h"):
            fmt_spec = fmt_spec[:-1]
            coords = itertools.chain([abs(self)], self.angles())
            outer_fmt = "<{}>"
        else:
            coords = self
            outer_fmt = "({})"
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(", ".join(components))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)
