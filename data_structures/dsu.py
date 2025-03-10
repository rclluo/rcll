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
