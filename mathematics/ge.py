from numbers import Number
from vector import Vector2D
from math import sqrt

class Line():
    """
    A line in 2D space.
    """
    def __init__(self, a, b) -> None:
        """
        y=ax+b
        a is slope, b is y-intercept
        """
        if isinstance(a, Number) and isinstance(b, Number):
            self.a=a
            self.b=b
        else:
            raise TypeError("A and B must be numbers.")

    @classmethod
    def from_point_slope(cls, a: Vector2D, b):
        return cls(b, a.y-b*(a.x))

    @classmethod
    def from_two_points(cls, a: Vector2D, b: Vector2D):    
        a=Vector2D.from_packed_coords(a)
        b=Vector2D.from_packed_coords(b)
        diff=b-a
        return cls.from_point_slope(a,diff.y/diff.x)

    def distance(self, p: Vector2D):
        """
        y=ax+b
        ax-y+b=0
        """
        return (self.a*p.x-p.y+self.b)/(sqrt(self.a**2+1))

    def __contains__(self, p: Vector2D):
        return p.y==self.a*p.x+self.b

    def __str__(self):
        return str({"slope":self.a,"y-intercept":self.b})

print(Line(1,2))