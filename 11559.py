from collections import deque
board = [list(input()) for _ in range(12)]
new_board = [deque([0 for _ in range(12)]) for _ in range(6)]

for i in range(12):
    for j in range(6):
        new_board[j][i] = board[i][j]

board = new_board

dx = [1,-1,0,0]
dy = [0,0,1,-1]
def neighbors(u, visited):
    x, y = u
    for a, b in zip(dx, dy):
        newx, newy = x + a, y+b
        if newx >= 0 and newy>= 0 and newx < 6 and newy < 12 and not visited[newx][newy]:
            yield [newx, newy]

def bfs(u, board, visited):
    queue = deque()
    queue.append(u)
    visited[u[0]][u[1]] = True
    result = []
    color = board[u[0]][u[1]]
    while queue:
        v = queue.popleft()
        result.append(v)
        for k in neighbors(v, visited):
            if color == board[k[0]][k[1]]:
                visited[k[0]][k[1]] = True
                queue.append(k)
    return result
        
def find_not_visited(board, visited):
    for i in range(6):
        for j in range(11,-1,-1):
            if board[i][j] != '.':
                if not visited[i][j]:
                    return [i, j]
    return None

def find_puyo():
    visited = [[False for _ in range(12)] for _ in range(6)]
    puyo = []
    while True:
        u = find_not_visited(board, visited)
        if u is None:
            break
        temp = bfs(u, board, visited)
        if len(temp) >= 4:
            puyo.append(temp)
        # else:
        #     for x, y in temp:
        #         visited[x][y] = False
    return puyo
            
def pop_puyo(puyos):
    for puyo in puyos:
        for x, y in puyo:
            board[x][y] = '.'

def fall_down():
    for i in range(6):
        row = board[i]
        new_row = deque()
        for j in range(11,-1,-1):
            if row[j] != '.':
                new_row.appendleft(row[j])
        for _ in range(12 - len(new_row)):
            new_row.appendleft('.')
        board[i] = new_row
        
            
def solution():
    cnt = 0
    while True:
        puyos = find_puyo()
        if len(puyos) == 0:
            break
        cnt += 1
        pop_puyo(puyos)
        fall_down()
    print(cnt)
    
solution()

    