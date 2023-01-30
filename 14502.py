# 안전 지역은 벽 제외
import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline

N, M =  map(int, input().split())

map_area = [list(map(int, input().split())) for _ in range(N)]

available_location = []
virus = []
walls = []

for i in range(N):
    for j in range(M):
        if map_area[i][j] == 0:
            available_location.append((i, j))
        elif map_area[i][j] == 2:
            virus.append((i, j))
        else:
            walls.append((i, j))
            
            


def bfs_wrapper():
    visited = [[False for _ in range(M)] for _ in range(N)]
    for x, y in virus:
        visited[x][y] = True
    for x, y in walls:
        visited[x][y] = True
    
    virus_area = 0
    for u in virus:
        virus_area += bfs(u, visited)
    return virus_area


def neighbors(u):
    x, y = u
    if x - 1>=0:
        yield x - 1, y
    if y - 1>=0:
        yield x , y - 1
    if x+ 1 < N:
        yield x + 1, y
    if y + 1 < M:
        yield x, y + 1

def bfs(u, visited):
    queue = deque()
    queue.append(u)
    cnt = 1
    while queue:
        v = queue.pop()
        for neighbor in neighbors(v):
            if not visited[neighbor[0]][neighbor[1]]:
                visited[neighbor[0]][neighbor[1]] = True
                queue.append(neighbor)
                cnt +=1
    return cnt
        
    
    
min_val = M * N

for loc1, loc2, loc3 in combinations(available_location, 3):
    # map_area[loc1[0]][loc1[1]] = 1
    # map_area[loc2[0]][loc2[1]] = 1
    # map_area[loc3[0]][loc3[1]] = 1
    walls.extend([loc1, loc2, loc3])
    temp = bfs_wrapper()
    # print(temp)
    min_val = min(min_val, temp)
    
    walls.pop()
    walls.pop()
    walls.pop()
    
    
print(N * M - min_val - 3 -len(walls))
    