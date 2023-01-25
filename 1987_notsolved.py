#계속 시간초과 

import sys
input = sys.stdin.readline
R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
alphabet_visited = [False for _ in range(26)]

def get_alphabet_index(a):
    return ord(a) - 65


def neighbors(u):
    x, y  = u
    if x - 1 >= 0:
        yield x-1, y
    if y - 1>= 0:
        yield x , y - 1
    if x + 1 < R:
        yield x + 1, y
    if y + 1 < C:
        yield x, y + 1

def check_visited(u):
    x, y = u
    return alphabet_visited[get_alphabet_index(board[x][y])]        

def set_visited(u, visited = True):
    x, y = u
    alphabet_visited[get_alphabet_index(board[x][y])]  = visited     
    
max_count  = 0
count = 0 
def dfs(u):
    global count
    global max_count
    set_visited(u)
    count += 1
    no_neighbor = True
    for neighbor in neighbors(u):
        if not check_visited(neighbor):
            dfs(neighbor)
            no_neighbor = False
    
    if no_neighbor:
        max_count = (max_count, count)
        
    count -= 1
    set_visited(u, visited=False)
    
dfs((0, 0))
print(max_count)