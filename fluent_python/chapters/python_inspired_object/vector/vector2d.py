import math
from array import array

class Vector2D:
    typecode = 'd'
    # Работа с позиционными образцами
    __match_args__ = ('x', 'y')
    __slots__ = ('__x', '__y')

    def __init__(self, x=0, y=0):
        self.__x = float(x)
        self.__y = float(y)
    
    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        return (value for value in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)
    
    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + 
                bytes(array(self.typecode, self)))
    
    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)
    
    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector2D(x, y)
    
    def __mul__(self, scalar):
        return Vector2D(self.x * scalar, self.y * scalar)

    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('p'):
            fmt_spec = fmt_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = '<{}, {}>'
        else:
            coords = self
            outer_fmt = '({}, {})'
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(*components)
    
    def angle(self):
        return math.atan2(self.y, self.x)

    def __hash__(self):
        return hash((self.x, self.y))

    def __complex__(self):
        return complex(self.x, self.y)

    @classmethod
    def frombytes(cls, octets): # Вместо self передаётся сам класс
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)