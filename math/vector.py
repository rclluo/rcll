from numbers import Number
from math import sqrt, sin, cos
from infix import Infix

class Vector2D:
    def __init__(self, x: Number, y: Number):
        assert isinstance(x, Number)
        assert isinstance(y, Number)
        self.x=x
        self.y=y
    
    @classmethod
    def from_packed_coords(cls, i):
        assert hasattr(i,"__getitem__")
        assert len(i)==2
        return cls(i[0],i[1])
    
    @classmethod
    def from_polar(cls, r, theta):        
        return cls(r*cos(theta),r*sin(theta))
    
    def swap(self):
        z=self.x
        self.x=self.y
        self.y=z

    def magnitude(self):
        return sqrt(self.x**2+self.y**2)

    def unit(self):
        return self/self.magnitude()

    def __getitem__(self, key):
        assert key==0 or key==1
        if key==0:
            return self.x
        else:
            return self.y
    
    def __iter__(self):
        return iter((self.x,self.y))

    def __str__(self):
        return str(tuple(self))

    def __mul__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.x*other.x-self.y*other.y,self.x*other.y+self.y*other.x)
        elif isinstance(other, Number):
            return Vector2D(self.x*other,self.y*other)
        else:
            raise TypeError
    
    def __rmul__(self, other):
        return self*other

    def __truediv__(self, other):
        if isinstance(other, Number):
            return self*(1/other)
        else:
            raise TypeError
    
    def __add__(self, other):
        assert isinstance(other, Vector2D)
        return Vector2D(self.x+other.x,self.y+other.y)
    
    def __sub__(self, other):
        assert isinstance(other, Vector2D)
        return self+(-1*other)
    
    def __eq__(self, other):
        if hasattr(other,"__getitem__"):
            return self.x==other[0] and self.y==other[1]
        else:
            return False
        
def dot_product(a: Vector2D, b: Vector2D):
    return a.x*b.x+a.y*b.y

dot=Infix(dot_product)
