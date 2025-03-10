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
