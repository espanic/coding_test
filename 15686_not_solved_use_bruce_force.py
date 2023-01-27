import sys

input = sys.stdin.readline

N, M = map(int, input().split())
city_info = [list(map(int, input().split())) for _ in range(N)]
houses = []
chickens = {}
for i in range(N):
    for j in range(N):
        if city_info[i][j] == 1:
            houses.append([i, j])
        elif city_info[i][j] == 2:
            chickens[(i, j)] = 0
            
            

def neighbors(u):
    x, y  = u
    if x - 1 >= 0:
        yield x - 1, y
    if y - 1>= 0 :
        yield x , y - 1
    if x +1 < N:
        yield x+ 1, y
    if y + 1 < N:
        yield x, y + 1
        
def dfs(u):
    visited = [[False for _ in range(N)] for _ in range(N)]
    buffer = [u]
    visited[u[0]][u[1]] = True
    # depth = 0
    while buffer:
        # depth += 1
        temp = []
        chicken_points = False
        for e in buffer:
            # e_info = city_info[e[0]][e[1]]
            for neighbor in neighbors(e):
                x, y = neighbor
                if not visited[x][y]:
                    info = city_info[x][y]
                    if info == 2:
                        chicken_points = True
                        chickens[(x, y)] += 1
                    visited[x][y] = True
                    temp.append(neighbor)
        if chicken_points:
            buffer = None
        else:
            buffer = temp
                    
def dfs_cal(u):
    visited = [[False for _ in range(N)] for _ in range(N)]
    buffer = [u]
    visited[u[0]][u[1]] = True
    depth = 0
    while buffer:
        depth += 1
        temp = []
        chicken_points = False
        for e in buffer:
            for neighbor in neighbors(e):
                x, y = neighbor
                if not visited[x][y]:
                    info = city_info[x][y]
                    if info == 2:
                        return depth
                    visited[x][y] = True
                    temp.append(neighbor)
        buffer = temp

    
    

# house 마다 치킨 거리
for house in houses:
    dfs(house)

    
chickens_arr = sorted(chickens.items(), key=lambda x : x[1], reverse= True)
chickens_arr = chickens_arr[:M]
# print(chickens_arr)

#폐업시킨다. 
for loc in chickens.keys():
    city_info[loc[0]][loc[1]] = 0
for loc, _ in chickens_arr:
    x, y = loc
    city_info[x][y] = 2

result = 0
for house in houses:
    v = dfs_cal(house)
    # print(v)
    result += v
    
print(result)

