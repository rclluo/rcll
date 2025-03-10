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

class Polygon():
    """
    A Polygon
    """
    def __init__(self, verticies):
        """
        Verticies must be given in order, or sidelength and area returns will be inaccurate
        """
        if hasattr(verticies,"__iter__"):
            self.verticies=[Vector2D(v) for v in verticies]
            self.vertex_count=len(self.verticies)
            self.sidelength=[(self.verticies[i]-self.verticies[i-1]).magnitude() for i in range(self.vertex_count)]
        else:
            raise TypeError("verticies must be an iterable")
    
    def area(self):
        """
        Signed area by the shoelace formula
        """
        return sum([
            (self.verticies[i+1][0]-
             self.verticies[i][0])*
            (self.verticies[i+1][1]+
             self.verticies[i][1]) 
             for i in range(self.vertex_count)])/2

class Triangle(Polygon):
    """
    A triangle
    """
    def __init__(self, verticies):
        if len(verticies)==3:
            super().__init__(verticies)
        else:
            raise ValueError("Must have 3 verticies")
    
    def semiperimeter(self):
        return sum(self.sidelength)/2

    def area_heron(self):
        s=self.semiperimeter()
        return sqrt(
            s*
            (s-self.sidelength[0])*
            (s-self.sidelength[1])*
            (s-self.sidelength[2])
        )
