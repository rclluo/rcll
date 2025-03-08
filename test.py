from numbers import Number
from math import sqrt, sin, cos

"""
Prefix Sums
Please note that these functions take padded input and give padded output.
"""

def prefix_1d(arr: list) -> list:
    pref=[0 for i in range(len(arr))]
    for i in range(1, len(arr)):
        pref[i]=arr[i]+pref[i-1]
    return pref

def prefix_2d(arr: list[list]) -> list[list]:
    pref=[[0 for i in range(len(arr[0]))] for j in range(len(arr))]
    for i in range(1, len(arr)):
        for j in range(1, len(arr[0])):
            pref[i][j]=arr[i][j]+pref[i-1][j]+pref[i][j-1]-pref[i-1][j-1]
    return pref

def prefix_3d(arr: list[list[list]]) -> list[list[list]]:
    pref=[[[0 for i in range(len(arr[0][0]))] for j in range(len(arr[0]))] for k in range(len(arr))]
    for i in range(1, len(arr)):
        for j in range(1, len(arr[0])):
            for k in range(1, len(arr[0][0])):
                pref[i][j]=arr[i][j]+pref[i-1][j][k]+pref[i][j-1][k]+pref[i][j][k-1]-pref[i-1][j-1][k]-pref[i][j-1][k-1]-pref[i-1][j][k-1]+pref[i-1][j-1][k-1]
    return pref

"""
Frequency Array
"""

def freq(ls: list, key: lambda a:a):
    ret={}
    for i in ls:
        k=key(i)
        if k in ret:
            ret[k]+=1
        else:
            ret[k]=1

"""
Subsequence related things
"""

def lis(seq,comp=lambda a,b:a>b):
    """
    Longest Increasing Subsequence
    """
    if not seq:
        return seq
    m=[None]*len(seq)
    p=[None]*len(seq)
    l=1
    m[0]=0
    for i in range(1, len(seq)):
        lower=0
        upper=l
        if comp(seq[i],seq[m[upper-1]]):
            j=upper
        else:
            while upper-lower>1:
                mid=(upper+lower)//2
                if comp(seq[i],seq[m[mid-1]]):
                    lower=mid
                else:
                    upper=mid
            j=lower
        p[i]=m[j-1]
        if j==l or comp(seq[i],seq[m[j]]):
            m[j]=i
            l=max(l, j+1)
    result=[]
    pos=m[l-1]
    for _ in range(l):
        result.append(seq[pos])
        pos=p[pos]
    return result[::-1]

def lcs(a: list, b: list):
    """
    Longest Common Subsequence
    """
    m=len(a)
    n=len(b)
    l=[[0 for x in range(n+1)] for x in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                l[i][j]=0
            elif a[i-1]==b[j-1]:
                l[i][j]=l[i-1][j-1]+1
            else:
                l[i][j]=max(l[i-1][j], l[i][j-1])
    index=l[m][n]
    dp=[None]*(index+1)
    i=m
    j=n
    while i>0 and j>0:
        if a[i-1]==b[j-1]:
            dp[index-1]=a[i-1]
            i-=1
            j-=1
            index-=1
        elif l[i-1][j]>l[i][j-1]:
            i-=1
        else:
            j-=1
    return dp[:-1]

"""
Matrix Transformations
"""

def rotate(arr: list[list], rotations: int):
    """
    Rotate clockwise 90 degrees `rotations` times
    """
    for _ in range(rotations%4):
        arr=list(zip(*arr[::-1]))
    return arr

def flip_horizontal(arr: list[list]):
    return [i[::-1] for i in arr]

def flip_vertical(arr: list[list]):
    return arr[::-1]

class DSU:
    """
    Disjoint Set Union
    """
    def __init__(self, size: int) -> None:
        self.parents=[i for i in range(size)]
        self.sizes=[1 for _ in range(size)]
        self.size=size
    
    def find(self, x: int) -> int:
        if self.parents[x]==x:
            return x
        self.parents[x]=self.find(self.parents[x])
        return self.parents[x]
    
    def unite(self, x: int, y: int) -> bool:
        x_root=self.find(x)
        y_root=self.find(y)
        if x_root==y_root:
            return False
        if self.sizes[x_root]<self.sizes[y_root]:
            x_root, y_root=y_root, x_root
        self.parents[y_root]=x_root
        self.sizes[x_root]+=self.sizes[y_root]
        return True
    
    def connected(self, x: int, y: int) -> bool:
        return self.find(x)==self.find(y)
    
    def __str__(self):
        mp={}
        for i in range(self.size):
            if i in mp:
                mp[i].add(self.find(i))
            else:
                mp[i]={self.find(i)}
        first=True
        ret='{'
        for i in mp:
            if first:
                ret+=str(i)+": "+str(mp[i])+'\n'
                first=False
            else:
                ret+=' '+str(i)+": "+str(mp[i])+'\n'
        ret=ret[:-1]
        ret+='}'
        return ret

class LLNode:
    def __init__(self, data):
        self.data=data
        self.next=None

class LinkedList():
    """
    Linked List
    """

    def __init__(self):
        self.head=None

    def insert_front(self, data):
        new_node=LLNode(data)
        new_node.next=self.head
        self.head=new_node

    def insert_end(self, data):
        new_node=LLNode(data)
        if self.head is None:
            self.head=new_node
            return
        current_node=self.head
        while current_node.next:
            current_node=current_node.next
        current_node.next=new_node

    def insert_index(self, data, index=-1):
        if index==0:
            self.insert_front(data)
            return
        if index==-1:
            self.insert_end(data)
            return
        position=0
        current_node=self.head
        while current_node is not None and position+1 != index:
            position+=1
            current_node=current_node.next

        if current_node is not None:
            new_node=LLNode(data)
            new_node.next=current_node.next
            current_node.next=new_node
        else:
            raise IndexError

    def update(self, val, index):
        current_node=self.head
        position=0
        while current_node is not None and position != index:
            position+=1
            current_node=current_node.next

        if current_node is not None:
            current_node.data=val
        else:
            raise IndexError

    def pop_front(self):
        if self.head is None:
            return
        self.head=self.head.next

    def pop_back(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head=None
            return
        current_node=self.head
        while current_node.next and current_node.next.next:
            current_node=current_node.next
        current_node.next=None
    
    def pop(self, index=0):
        if self.head is None:
            return
        if index==0:
            self.pop_front()
            return
        if index==-1:
            self.pop_back()
            return
        current_node=self.head
        position=0
        while current_node is not None and current_node.next is not None and position+1 != index:
            position+=1
            current_node=current_node.next

        if current_node is not None and current_node.next is not None:
            current_node.next=current_node.next.next
        else:
            raise IndexError

    def remove_node(self, data):
        current_node=self.head
        if current_node is not None and current_node.data==data:
            self.pop_front()
            return
        while current_node is not None and current_node.next is not None:
            if current_node.next.data==data:
                current_node.next=current_node.next.next
                return
            current_node=current_node.next
        raise ValueError

    def size(self):
        size=0
        current_node=self.head
        while current_node:
            size+=1
            current_node=current_node.next
        return size

    def __str__(self):
        return str(list(self))
    
    def __iter__(self):
        ret=[]
        current_node=self.head
        while current_node:
            ret.append(current_node)
            current_node=current_node.next
        return iter(ret)

class TrieNode:
    def __init__(self):
        self.children=[None]*128
        self.is_end=False

class Trie:
    """
    Trie/Prefix Tree
    """

    def __init__(self):
        self.words=set()
        self.root=TrieNode()

    def insert(self, key):
        self.words.add(key)
        print(self.words)
        curr=self.root
        for c in key:
            index=ord(c)
            if curr.children[index] is None:
                new_node=TrieNode()
                curr.children[index]=new_node
            curr=curr.children[index]
        curr.is_end=True

    def search(self, key) -> bool:
        curr=self.root
        for c in key:
            index=ord(c)
            if curr.children[index] is None:
                return False
            curr=curr.children[index]
        return curr.is_end
    
    def __str__(self):
        return '{'+", ".join(self.words)+'}'

class Infix:
    def __init__(self, func, lhs=None):
        self.func=func
        self.lhs=lhs

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

    def __ror__(self, lhs):
        return __class__(self.func, lhs)

    def __or__(self, rhs):
        return self(self.lhs, rhs)

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

    @classmethod
    def from_packed_polar(cls, i):
        assert hasattr(i,"__getitem__")
        assert len(i)==2
        return cls.from_polar(i[0],i[1])
    
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
    
    def __len__(self):
        return 2
        
def dot_product(a: Vector2D, b: Vector2D):
    return a.x*b.x+a.y*b.y

dot=Infix(dot_product)

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

calc_primes_upto=5000000
primes=[]

def prime_factorization(n: int) -> list[int]:
    global primes
    pf=[]
    if not len(primes):
        primes=find_primes(calc_primes_upto)
    for p in primes:
        if n%p==0:
            e=0
            while n%p==0:
                n//=p
                e+=1
            pf.append((p,e))
        if p*p>n: 
            break
    if n>1:
        pf.append((n,1))
    return pf

def find_primes(n: int) -> list[int]:
    if n<=2:
        return []
    sieve=list(range(3, n, 2))
    top=len(sieve)
    for si in sieve:
        if si:
            bottom=(si*si-3)//2
            if bottom>=top:
                break
            sieve[bottom::si]=[0]*-((bottom-top)//si)
    return [2]+[el for el in sieve if el]

def factor_count(n: int) -> int:
    pf=prime_factorization(n)
    num_factors=1
    for _, e in pf:
        num_factors*=(e+1)
    return num_factors

def euler_totient(n: int) -> int:
    pf=prime_factorization(n)
    ret=n
    for p, _ in pf:
        ret*=(p-1)
        ret//=p
    return ret