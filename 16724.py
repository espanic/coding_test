from enum import Enum

class Status(Enum):
    visited = 0
    tracking = 1
    not_visited = 2

N, M = map(int, input().split())

board = [list(input()) for _ in range(N)]

visited = [[Status.not_visited for _ in range(M)] for _ in range(N)]

dx = [1,-1,0,0]
dy = [0,0,1,1]

def yield_can_go(u):
    x, y = u
    if board[x][y] == 'U':
        return x -1, y
    if board[x][y] == 'D':
        return x+1, y
    if board[x][y] == 'L':
        return x, y-1
    else:
        return x, y+1

cnt = 0
def dfs(u):
    global cnt
    visited[u[0]][u[1]] = Status.tracking
    v = yield_can_go(u)
    
    status = visited[v[0]][v[1]]
    if status == Status.not_visited:
        dfs(v)
    elif status == Status.tracking:
        cnt += 1
    # else:
    #     cnt += 1
        
    visited[u[0]][u[1]] = Status.visited
        
        
for i in range(N):
    for j in range(M):
        if visited[i][j] == Status.not_visited:
            dfs([i,j])
print(cnt)