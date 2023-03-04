N = int(input())
node_key = list(map(int, input().split()))
X = int(input())
nodes = [Node(i) for i in node_key]

p = None

for i, node in enumerate(nodes):
    node.left = nodes[2*i +1]
    node.right = nodes[2*i+2]
    if i != 0:
        node.parent = nodes[(i -1) // 2]
    if node.key == -1:
        node.key = X
        p = i



class Node:
    def __init__(self, key, left = None, right=None, parent = None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent


class BinaryTree:
    def __init__(self, nodes):
        self.root = nodes[0]
        
    def go_up(self, p):
        if p != 0:
            
            parent_ind = (p-1) // 2
            parent_val = nodes[parent_ind].key
            left_ind = parent_ind*2 +1
            right_ind = parent_ind* 2 + 2
            
            left_left_child = nodes[left_ind].left
            left_right_child = nodes[right_ind].right
            right_right_child = nodes[right_ind].right
            right_left_child = nodes[right_ind].left
            
            
            
            temp = [parent_ind, left_ind, right_ind]
            temp.sort(key=lambda x: nodes[x].key)
            
            nodes[temp[0]].left = left_left_child
            nodes[temp[0]].right = left_right_child
            nodes[temp[1]].left = nodes[temp[0]]
            nodes[temp[1]].right = nodes[temp[2]]
            nodes[temp[2]].left = right_left_child
            nodes[temp[3]].right = right_right_child
            if parent_val != node[temp[1]].key:
                self.go_up(parent_ind)
                
    def go_down(q = 0):
        if 2*q + 2 < N:
            me = q
            left = 2*q +1
            right = 2*q +2
            temp = [me, left, right]
            if nodes[me].key > nodes[right].key:
                
                

            
            
            
            
            
        
        
        
tree = BinaryTree(nodes)


    
