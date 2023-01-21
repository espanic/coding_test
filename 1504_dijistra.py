import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
N, E = map(int, input().split())


# edges = [[INF] * N for _ in range(N)]

# for i in range(E):
#     left, right, distance = map(int, input().split())
#     edges[left - 1][right - 1] = distance
#     edges[right - 1][left - 1] = distance

edges_temp = [[] for _ in range(N)]
for i in range(E):
    left, right, dist = map(int, input().split())
    edges_temp[left - 1].append([right, dist])
    edges_temp[right - 1].append([left, dist])

v1, v2 = map(int, input().split())



## 아직 해결안됨!!!


def dijistra(start, dest):
    vertices = [INF] * N
    heap  = []
    vertices[start - 1] = 0
    heapq.heappush(heap, [vertices[start - 1], start])
    while heap:
        dist, v = heapq.heappop(heap)
        if v == dest:
            return dist
        for k, w in edges_temp[v - 1]:
            if vertices[ k - 1] > dist + w:
                vertices[k - 1] = dist + w
                heapq.heappush(heap, [vertices[k - 1], k])
            
        
        
    return -1


# 1->v1 -> v2 -> N
res1 = - 1
start_to_v1 = dijistra(1, v1)
if start_to_v1 != -1:
    v1_to_v2 = dijistra(v1, v2)
    if v1_to_v2 != -1:
        v2_to_n = dijistra(v2, N)
        if v2_to_n != -1:
            res1 = start_to_v1 + v1_to_v2 + v2_to_n



# 1->v2 -> v1 -> N
res2 = - 1
start_to_v2 = dijistra(1, v2)
if start_to_v2 != -1:
    v2_to_v1 = dijistra(v2, v1)
    if v2_to_v1 != -1:
        v1_to_n = dijistra(v1, N)
        if v1_to_n != -1:
            res2 = start_to_v2 + v2_to_v1 + v1_to_n
            
if res1 == - 1 and res2 == -1:
    print(-1)
else:
    print(min(res1, res2))


