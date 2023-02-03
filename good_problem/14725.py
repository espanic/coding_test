import sys
input = sys.stdin.readline
N = int(input())


class Vertex:
    def __init__(self, letter, level):
        self.letter = letter
        self.level = level
        self.children = []
        
    def __eq__(self, other):
        return self.letter == other.letter and self.level == other.level
    
    def __hash__(self) -> int:
        return hash(self.letter) ^ hash(self.level)

preyInfoTemp = []
max_level = 1
for _ in range(N): 
    temp = list(input().split())
    max_level = max(max_level, int(temp[0]))
    preyInfoTemp.append(temp[1:])
    
prey_grid = [[None for _ in range(max_level)] for _ in range(N)]

for i, temp in enumerate(preyInfoTemp):
    for j, s in enumerate(temp):
        prey_grid[i][j] = s

del preyInfoTemp

roots = set()
for i in range(N):
    roots.add(Vertex( prey_grid[i][0],0))
roots = list(roots)


def placing(parent, vertex):
    children = parent.children
    alreadyIn = False
    for child in children:
        if child == vertex:
            vertex = child
            alreadyIn = True
            break
    if not alreadyIn:
        children.append(vertex)
    return vertex
    
        
    
def find_parent(s):
    for root in roots:
        if root.letter == s:
            return root



if max_level > 1:
    for i in range(N):
        j = 1
        vertex = Vertex(prey_grid[i][j], j)
        
        parent = find_parent(prey_grid[i][j-1])
        while True:
            parent = placing(parent, vertex)
            if j + 1 < max_level and prey_grid[i][j + 1] is not None:
                j += 1
                vertex = Vertex(prey_grid[i][j], j)
            else:
                break

roots = sorted(roots, key= lambda x: x.letter)

def print_info(vertex):
    level = vertex.level
    s = "--" * level + vertex.letter
    print(s)
    children = sorted(vertex.children,key= lambda x: x.letter)
    for child in children:
        print_info(child)

for root in roots:
    print_info(root)
        

    

    

    




             



