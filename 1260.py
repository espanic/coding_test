from collections import deque

n, m, v = map(int, input().split())
edges_temp = [list(map(int, input().split())) for _ in range(m)]
edges = [[] for _ in range(n)]

for edge in edges_temp:
    left, right = edge
    edges[left - 1].append(right)
    edges[right - 1].append(left)
    
for edge in edges:
    edge.sort()


# dfs
visited = [False for _ in range(n)]
# stack = deque([])
# stack.append(v)
dfs_result = []
# while len(stack) != 0:
#     u = stack.pop()
#     if visited[u - 1]:
#         continue
#     visited[u-1] = True
#     dfs_result.append(u)
#     edges_u = edges[u-1]
#     for i in range(len(edges_u)-1, -1, -1):
#         dest = edges_u[i]
#         if not visited[dest - 1]:
#             stack.append(dest)
            

# without stack
def dfs(u):
    visited[u - 1] = True
    dfs_result.append(u)
    for vertex in edges[u-1]:
        if not visited[vertex - 1]:
            dfs(vertex)
            
dfs(v)


# bfs
queue = deque([])
visited = [False for _ in range(n)]

visited[v-1] = True
queue.append(v)
bfs_result = [v]
while len(queue) != 0:
    u = queue.popleft()
    for dest in edges[u - 1]:
        if not visited[dest - 1]:
            queue.append(dest)
            visited[dest - 1] = True
            bfs_result.append(dest)
            
            

for i, vertex in enumerate(dfs_result):
    if i != len(dfs_result) - 1:
        print(vertex, end=" ")
    else:
        print(vertex)
        
for i, vertex in enumerate(bfs_result):
    if i != len(bfs_result) - 1:
        print(vertex, end=" ")
    else:
        print(vertex)
