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
