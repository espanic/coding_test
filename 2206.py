from collections import deque


N , M = map(int, input().split())

board = [list(map(int, list(input()))) for _ in range(N)]
min_dists = [[None for _ in range(M)] for _ in range(N)]



walls = [None]


for i in range(N):
    for j in range(M):
        if board[i][j]:
            walls.append((i, j))


def neighbors(u):
    x, y = u
    if x - 1 >= 0:
        yield x- 1, y
    if y - 1 >=0 :
        yield x, y-1
    if x + 1 < N:
        yield x + 1, y
    if y + 1 < M:
        yield x, y + 1
        
        
def bfs(u):
    answer = -1
    visited = [[[0, 0] for _ in range(M)] for _ in range(N)]

    queue = deque()
    queue.append((u, 0))
    visited[u[0]][u[1]][0] = 1
    while queue:
        v , crash= queue.popleft()
        # print(v, crash,visited[v[0]][v[1]][crash])
        if v[0] == N - 1 and v[1] == M - 1:
            answer = visited[v[0]][v[1]][crash]
            break
        for k in neighbors(v):
                if not visited[k[0]][k[1]][crash] and not board[k[0]][k[1]]:
                    visited[k[0]][k[1]][crash] = visited[v[0]][v[1]][crash] + 1
                    queue.append((k, crash))
                else:
                    if crash == 0 and not visited[k[0]][k[1]][1]:
                        visited[k[0]][k[1]][1] = visited[v[0]][v[1]][0] + 1
                        queue.append((k, 1))
     
                
    return answer

print(bfs((0,0)))

