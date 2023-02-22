import heapq
from collections import deque
N, Q = map(int, input().split())
INF = float('inf')
edges = [[] for _ in range(N)]




    
def bfs(u, k):
    weight = [None for _ in range(N)]
    visited = [False for _ in range(N)]
    queue = deque()
    weight[u] = INF
    queue.append([u, INF])
    visited[u] = True
    while queue:
        v, prev_usado = queue.popleft()
        for w, usado in edges[v]:
            if not visited[w]:
                weight[w] = min(prev_usado, usado)
                visited[w] = True
                queue.append([w, weight[w]])
    
    cnt = 0
    for i in weight:
        if i >= k:
            cnt += 1
    return cnt - 1
        

    
for _ in range(Q):
    k,v = map(int, input().split())
    v -= 1
    answer = bfs(v, k)
    print(answer)