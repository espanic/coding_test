import sys
from collections import deque
input = sys.stdin.readline
location = None
N = int(input())
space = []
for i in range(N):
    rec = list(map(int, input().split()))
    if 9 in rec:
        location = [i, rec.index(9)]
        rec[location[1]] = 0
    space.append(rec)
        
visited = [[False for _ in range(N)] for _ in range(N)]



def neighbors(u):
    x, y = u
    
    if y - 1 >=0:
        yield x, y - 1
        
    if x - 1 >= 0:
        yield x - 1, y
        
    if y + 1 < N:
        yield x , y + 1
        
    if x + 1 < N:
        yield x + 1, y
        
    
        
def check_valid_fish():
    fish = []
    for i, row in enumerate(space):
        for j,e in enumerate(row):
            if e!=0 and e < size:
                fish.append([i, j])
    return fish
    
        
def bfs(location, size):
    count = 0
    queue = deque()
    queue.append(location)
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[location[0]][location[1]] = True
    while queue:
        temp = deque()
        can_eat = []
        for u in queue:
            for neighbor in neighbors(u):
                x, y = neighbor
                if not visited[x][y]:
                    if space[x][y] == size or space[x][y] == 0:
                        temp.append(neighbor)
                        visited[x][y] = True
                    elif space[x][y] < size:
                        can_eat.append(neighbor)
                        visited[x][y] = True
        if can_eat:
            can_eat.sort()
            return can_eat[0], count + 1
        else:
            queue = temp
        count += 1
    return None, 0
      
                    
result = 0
size = 2
size_buffer = 0
while True:
    location, count = bfs(location, size)

    # no fish available
    if not count:
        print(result)
        break
    result += count
    space[location[0]][location[1]] = 0
    size_buffer += 1
    if size  == size_buffer:
        size += 1
        size_buffer = 0
    
    
    


            
                
                
            
        


    