import heapq
N = int(input())
house = [list(input()) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0,  0,-1, 1]

def yield_available(u):
    x, y = u
    for _x, _y in zip(dx, dy):
        if check_bound([x+_x, y+_y]):
            yield x + _x, y + _y, _x, _y
            
def check_bound(u):
    x, y = u
    if x >= 0 and x < N and y >=0 and y < N:
        return True
    return False
            
def compute_mirror_dir(x, y):
    if x == 0:
        yield -1, 0
        yield 1, 0
    elif y == 0:
        yield 0, 1
        yield 0, -1




start, end = None, None

for i in range(N):
    for j in range(N):
        if house[i][j] == '#':
            if start is None:
                start = [i, j]
            else:
                end = [i, j]
                

def get_direction_index(u):
    x, y = u
    if x == 1 and y == 0:
        return 0
    if x == -1 and y == 0:
        return 1
    if x == 0 and y == 1:
        return 2
    if x == 0 and y == -1:
        return 3

INF = 1e9
                
def dijistra(start, end):
    heap = []
    visited = [[[INF for _ in range(4)] for _ in range(N)] for _ in range(N)]
    
    
    for x,y, _x, _y in yield_available(start):
        if house[x][y] == '*':
            continue
        elif house[x][y] == '.' or house[x][y] == '#':
            heapq.heappush(heap,[0, x, y, _x, _y])
            ind = get_direction_index((_x, _y))
            visited[x][y][ind] = 0


        else:
            heapq.heappush(heap,[0, x, y, _x, _y])
            ind = get_direction_index((_x, _y))
            visited[x][y][ind] = 0
            
            for new_dx, new_dy in compute_mirror_dir(_x, _y):
                ind = get_direction_index((new_dx, new_dy))
                if visited[x][y][ind] > 1:
                    visited[x][y][ind] = 1
                    heapq.heappush(heap,[1, x, y, new_dx,new_dy])
            
    while heap:
        dist, x, y, _x, _y = heapq.heappop(heap)

        if x == end[0] and y == end[1]:
            return dist
        
        new_x, new_y = x +_x, y + _y
        if not check_bound([new_x, new_y]):
            continue
        
        val = house[new_x][new_y]
        if val == '*':
            continue

        elif (val == '.' or val == '#'):
            ind = get_direction_index((_x, _y))
            if visited[new_x][new_y][ind] > dist:
                heapq.heappush(heap, [dist, new_x, new_y, _x, _y])
                visited[new_x][new_y][ind] = dist
        elif val == '!':
            ind = get_direction_index((_x, _y))
            if visited[new_x][new_y][ind] > dist:
                heapq.heappush(heap, [dist, new_x, new_y, _x, _y])
                visited[new_x][new_y][ind] = dist
                
            for new_dx, new_dy in compute_mirror_dir(_x, _y):
                ind = get_direction_index((new_dx, new_dy))
                if visited[new_x][new_y][ind] > dist + 1:
                    heapq.heappush(heap, [dist + 1, new_x, new_y, new_dx, new_dy])
                    visited[new_x][new_y][ind] = dist + 1
                    
    raise NameError("aa")
                
answer = dijistra(start, end)
print(answer)