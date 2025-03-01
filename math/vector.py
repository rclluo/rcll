from numbers import Number

class Vector2D:
    def __init__(self, x: Number, y: Number):
        assert isinstance(x, Number)
        assert isinstance(y, Number)
        self.x=x
        self.y=y
    
    @classmethod
    def from_packed(cls,i):
        assert hasattr(i,"__getitem__")
        assert len(i)==2
        return cls(i[0],i[1])

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

        elif isinstance(other, Number):

        else:
            raise TypeError