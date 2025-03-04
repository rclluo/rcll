from numbers import Number
from .vector import Vector2D
from math import sqrt

class Line():
    """
    A line in 2D space.
    """
    def __init__(self, a: Vector2D, b) -> None:
        """
        y=ax+b
        """
        self.a: Vector2D=Vector2D.from_packed_coords(a)
        if isinstance(b, Number):
            self.b=b
        else:
            raise TypeError("B must be a number")

    @classmethod
    def from_two_points(cls, a: Vector2D, b: Vector2D):    
        a=Vector2D.from_packed_coords(a)
        b=Vector2D.from_packed_coords(b)
        diff=b-a
        return cls(a,diff.y/diff.x)

    def distance(self, p: Vector2D):
        return (self.a*(self.a.x-p.x)+(self.a.y-p.y))/sqrt(self.b**2+1)

    def __contains__(self, p: Vector2D):
        diff=p-self.a
        return (diff.y/diff.x)==p.y

    def __add__(self, other):
        other=Vector2D(other)
        self.a+=other
    
    def __sub__(self, other):
        other=Vector2D(other)
        self.a-=other

    def __str__(self):
        return str({"point":self.a,"slope":self.b})