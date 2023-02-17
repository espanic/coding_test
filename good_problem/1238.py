import heapq

N, M, X = map(int, input().split())
X -= 1
edges = [[] for _ in range(N)]

for _ in range(M):
    start, end, t = map(int, input().split())
    start -= 1
    end -= 1
    edges[start].append([end,t])
    
INF = 1e9

def dijistra(start, end):
    heap = []
    weights = [INF for _ in range(N)]
    heap.append([0, start])
    weights[start] = 0
    
    while heap:
        dist, u = heapq.heappop(heap)
        if u == end:
            return dist
        for v, w in edges[u]:
            new_weight = dist + w
            if weights[v] > new_weight:
                heapq.heappush(heap, [new_weight,v])
                weights[v] = new_weight

max_time = 0
for i in range(N):
    val1, val2 = dijistra(i,X), dijistra(X, i)
    time_spent = val1 + val2
    max_time = max(max_time, time_spent)
    
print(max_time)