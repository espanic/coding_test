from collections import deque
R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
visited = [[False for _ in range(C)] for _ in range(R)]
visited_alphabets =[False for _ in range(26)]


def ascii_index(c):
    return ord(c) - 65

def neighbors(u):
    x, y = u
    if x - 1>= 0:
        yield x-1, y
    if y - 1>=0:
        yield x, y - 1
    if x + 1 < R:
        yield x+1, y
    if y + 1 < C:
        yield x, y+1

ans = 1
def bfs(u):
    global ans
    queue = deque()

    visited_char = set([board[u[0]][u[1]]])
    queue.append([u, 1, visited_char])
    # visited_alphabets[ascii_index(board[u[0]][u[1]])] = True
    while queue:
        v, dist, v_char = queue.popleft()
        for neighbor in neighbors(v):
            x, y = neighbor
            if board[x][y] not in v_char:
                ans = max(dist + 1, ans)
                queue.append([neighbor, dist + 1, v_char +board[x][y]])
         
bfs((0,0))   
print(ans)

    
    