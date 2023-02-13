import sys


class Node:
    def __init__(self, key):
        self.key = key
        self.children = []
        
        
    def getChildrenNode(self, c):
        for node in self.children:
            if node.key == c:
                return node
        return None
        
class Trie:
    def __init__(self):
        self.head = Node(None)
        self.leaf_cnt = 0
        
    def insert(self, string):
        curr = self.head
        leaf_added = False
        for i in range(len(string)):
            c = string[i]
            node = curr.getChildrenNode(c)
            if node is None:
                if curr == self.head or len(curr.children) != 0:
                    leaf_added = True
                node = Node(c)
                curr.children.append(node)
            curr = node
        if leaf_added:
            self.leaf_cnt += 1
        

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    
    
    phone_numbers = [list(input())[:-1] for _ in range(n)]
    trie = Trie()
    for phone in phone_numbers:
        trie.insert(phone)
    if trie.leaf_cnt == n:
        print("YES")
    else:
        print("NO")
            
    
