N, M = map(int, input().split())
edges = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append(b)

visited = [False for _ in range(N)]
result = []
def topological_sort(u):
    visited[u] = True
    for v in edges[u]:
        if not visited[v]:
            topological_sort(v)
    result.append(u+1)
    
    
for i in range(N):
    if not visited[i]:
        topological_sort(i)

result.reverse()
print(" ".join(map(str, result)))
    
    