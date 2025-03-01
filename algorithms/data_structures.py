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
        

class Trie:
    """
    Trie/Prefix Tree
    """
    class TrieNode:
        def __init__(self):
            self.children=[None]*128
            self.is_end=False

    def __init__(self):
        self.words=set()
        self.root=Trie.TrieNode()

    def insert(self, key):
        self.words.add(key)
        print(self.words)
        curr=self.root
        for c in key:
            index=ord(c)
            if curr.children[index] is None:
                new_node=Trie.TrieNode()
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
    
class LinkedList():
    """
    Linked List
    """
    class LLNode:
        def __init__(self, data):
            self.data=data
            self.next=None

    def __init__(self):
        self.head=None

    def insert_front(self, data):
        new_node=LinkedList.LLNode(data)
        new_node.next=self.head
        self.head=new_node

    def insert_end(self, data):
        new_node=LinkedList.LLNode(data)
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
            new_node=LinkedList.LLNode(data)
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