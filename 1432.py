import heapq

class Vertex():
    def __init__(self, key):
        self.key = key
        self.in_degree = 0
        self.edges = []


N = int(input())
board = [list(map(int,list(input()))) for _ in range(N)]
vertices = [Vertex(i) for i in range(N)]
visited = [False for _ in range(N)]


for i, row in enumerate(board):
    for j, val in enumerate(row):
        if val == 1:
            vertices[i].edges.append(vertices[j])
            vertices[j].in_degree += 1
            
heap = []
for i in range(N):
    if vertices[i].in_degree == 0:
        heapq.heappush(heap, [-vertices[i].key, vertices[i]])

def topological_sort():
    result = []
    while heap:
        _, vertex = heapq.heappop(heap)
        result.append(vertex.key)
        for child in vertex.edges:
                child.in_degree -= 1
                if child.in_degree == 0:
                    heapq.heappush(heap, [-child.key, child])

    if len(result) != N:
        return None
    return result

result = topological_sort()  
print(result)
if result == None:
    print(-1)
else:
    mapping = [None for _ in range(N)]
    for i, val in enumerate(result):
        mapping[val] = i + 1
    print(" ".join(map(str, mapping)))