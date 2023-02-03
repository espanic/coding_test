from collections import deque
R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
visited = [[False for _ in range(C)] for _ in range(R)]
visited_alphabets =[False for _ in range(26)]


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

ans = 0

                
                
def set_alphabet(a, val = True):
    i = ord(a) - 65
    visited_alphabets[i] = val
    


def dfs(u, depth):
    global ans
    ans = max(ans, depth)
    x, y = u
    c = board[x][y]
    # visited_alphabets.append(c)
    set_alphabet(c, val = True)
    
    for neighbor in neighbors(u):
        x, y = neighbor
        c = board[x][y]
        if not visited_alphabets[ord(c) - 65]:
            dfs(neighbor, depth + 1)
            set_alphabet(c, val=False)

    
dfs((0,0), 1)
print(ans)
    
    
    