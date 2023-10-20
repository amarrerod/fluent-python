from array import array
import math


class Vector2d:
    typecode = "d"
    # We include this to allow positional pattern matching
    # in match statements
    __match_args__ = ("x", "y")

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        """
        Hacemos x e y componentes de solo lectura
        para poder conseguir que Vector2d sea hashable
        """
        return self.__x

    @property
    def y(self):
        """
        Hacemos x e y componentes de solo lectura
        para poder conseguir que Vector2d sea hashable
        """
        return self.__y

    def __iter__(self):
        # return (i for i in (self.x, self.y))
        yield self.x
        yield self.y

    def __repr__(self):
        class_name = type(self).__name__
        return "{}({!r}, {!r})".format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __complex__(self):
        return complex("{0}{1:+}j".format(*self))

    def __bytes__(self):
        return bytes([ord(self.typecode)]) + bytes(array(self.typecode, self))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def angle(self):
        return math.atan2(self.y, self.x)

    def __bool__(self):
        return bool(abs(self))

    def __hash__(self):
        """
        The __hash__ special method documentation
        suggest computing the hash of a tuple with the
        components
        """
        return hash((self.x, self.y))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)

    def __format__(self, fmt_spec=""):
        if fmt_spec.endswith("p"):
            fmt_spec = fmt_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = "<{}, {}>"
        else:
            coords = self
            outer_fmt = "({}, {})"
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(*components)
