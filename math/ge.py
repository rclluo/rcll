from numbers import Number
from vector import Vector2D
from math import sqrt

class Line():
    """
    A line in 2D space.
    """
    def __init__(self, a: Vector2D, b) -> None:
        """
        y=ax+b
        """
        self.a: Vector2D=a
        if isinstance(b, Number):
            self.b=b
        else:
            raise TypeError("B must be a number")

    def distance(self, p: Vector2D):
        return (a*(self.a.x-p.x)+(self.a.y-p.y)))/sqrt(m**2+1)

    def __contains__(self, p: Vector2D):
        return self.a*p.x+self.b==p.y
