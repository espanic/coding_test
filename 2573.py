import sys
import copy
from collections import deque
input  = sys.stdin.readline
N, M = map(int, input().split())

npole = [list(map(int, input().split())) for _ in range(N)]
ice_mount = []

for i in range(N):
    for j in range(M):
        if npole[i][j] != 0:
            ice_mount.append((i, j))
            
            
def neighbors(u):
    x, y = u
    if x - 1 >= 0:
        yield x - 1, y
    if x + 1 < N:
        yield x + 1, y
    if y - 1 >= 0:
        yield x, y - 1
    if y + 1 < M:
        yield x, y + 1
        
def check_not_visited(visited):
    for i in range(N):
        for j in range(M):
            if not visited[i][j]:
                return (i, j)
    return None

def dfs(v, visited):
    visited[v[0]][v[1]] = True
    for neighbor in neighbors(v):
        if not visited[neighbor[0]][neighbor[1]]:
            dfs(neighbor, visited)
            
            
def bfs(v, visited):
    queue = deque()
    visited[v[0]][v[1]] = True
    queue.append(v)
    while queue:
        u = queue.popleft()
        for neighbor in neighbors(u):
            if not visited[neighbor[0]][neighbor[1]]:
                visited[neighbor[0]][neighbor[1]] = True
                queue.append(neighbor)
    
    
            
def count_zero(u, visited):
    res = 0
    for neighbor in neighbors(u):
        if visited[neighbor[0]][neighbor[1]] == True:
            res += 1
    return res
            
            
def melting(visited):
    global ice_mount
    global npole
    temp = []
    corrected = []
    # npole_temp = copy.deepcopy(npole)
    
    for x,y in ice_mount:
        visited[x][y] = False
    
    for mount in ice_mount:
        melting_val = count_zero(mount , visited)
        npole[mount[0]][mount[1]] = max(npole[mount[0]][mount[1]]  - melting_val , 0)
        if npole[mount[0]][mount[1]]:
            # visited[mount[0]][mount[1]] = False
            temp.append(mount)
        else:
            corrected.append(mount)
            
    for x, y in corrected:
        visited[x][y] = True
        

    ice_mount = temp
    return visited
            
def generate_visited():
    visited = [[False for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if npole[i][j] == 0:
                visited[i][j] = True
    return visited



# 문제시작
year = 0
visited = generate_visited()
while True:
    count = 0
    # 특수조건
    if not ice_mount:
        year = 0
        break
    for v in ice_mount:
        if not visited[v[0]][v[1]]:
            bfs(v, visited)
            count += 1
    if count < 2:
        year += 1
        visited = melting(visited)

    else:
        break

print(year)