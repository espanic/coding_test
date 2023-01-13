# 50분 걸림

from collections import deque
n, m = map(int, input().split())
# maze_temp = [list(map(int, input().split())) for _ in range(n)]

maze_temp = []
for _ in range(n):

    inputString  = input()
    row = []
    for j in range(m):
        row.append(int(inputString[j]))
    maze_temp.append(row)
    
    
visited = [[False] * m for _  in range(n)]
depth = [[0] * m for _  in range(n)]

def checkInBound(i, j):
    return i >=0 and i < n and j >= 0 and j < m

def getNeighborList(v):
    i, j = v
    neighbors = []
    
    if checkInBound(i, j + 1) and maze_temp[i][j+1]:
        neighbors.append((i, j + 1))


    if checkInBound(i, j - 1) and maze_temp[i][j-1]:
        neighbors.append((i, j - 1))


    if checkInBound(i + 1, j ) and  maze_temp[i + 1][j]:
        neighbors.append((i + 1, j))


    if checkInBound(i - 1, j ) and  maze_temp[i - 1][j]:
        neighbors.append((i - 1, j))

    return neighbors
    
    


def bfs():
    queue = deque()
    visited[0][0] = True
    queue.append((0, 0))

    while len(queue) != 0:
        v = queue.popleft()

        for neighbor in getNeighborList(v):
            x, y = neighbor
            if  not visited[x][y]:
                depth[x][y] += depth[v[0]][v[1]] + 1
                visited[x][y] = True
                queue.append(neighbor)
                if x == n - 1 and y == m - 1:
                    return depth[x][y] + 1

    return "error"
                

print(bfs())
        

    


