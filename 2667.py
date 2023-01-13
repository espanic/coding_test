import sys
from collections import deque


def splitString(str):
    result = []
    for i in range(N):
        result.append(int(str[i]))
    return result


readline = sys.stdin.readline
N = int(readline())
houses_grid_temp = [splitString(readline()) for _ in range(N)]
houses_grid = [[0] * N for _ in range(N)]
houses = []


# 각 집ㅡ 튜플로 저장
for i in range(N):
    for j in range(N):
        if houses_grid_temp[i][j]:
            houses.append([i, j, False])
        houses_grid[i][j] = houses_grid_temp[i][j]

# 집이 어느 단지에 속하는지에 대한 번호    
house_labels = [-1] * len(houses)



def check_not_labeled_houses(house_labels):
    result = []
    for house in houses:
        if not house[-1]:
            result.append(house)
    return result

def find_neighbors_not_visited(u, houses_sublist, visited):
    i, j, _ = u
    neighbors = []
    for k, house_tuple in enumerate(houses_sublist):
        x, y, _ = house_tuple
        if abs(x - i) + abs(y - j) == 1 and not visited[k]:
            house_tuple[-1] = True
            neighbors.append(house_tuple)
            visited[k] = True
    return neighbors
    
    
    

def dfs(houses_sublist):
    queue = deque()
    u = houses_sublist[0]
    visited = [False] * len(houses_sublist)
    queue.append(houses_sublist[0])
    visited[0] = True
    u[-1] = True
    count  = 1
    
    while len(queue) != 0:
        u = queue.popleft()
        neighbors = find_neighbors_not_visited(u, houses_sublist, visited)
        count += len(neighbors)
        for neighbor in neighbors:
            queue.append(neighbor)
    return count
            

label_counts = []
# 아직 라벨링되지 않은 집이 존재한다면
label = 0
while True:
    houses_sublist = check_not_labeled_houses(house_labels)
    if houses_sublist:
        label_counts.append(dfs(houses_sublist))
    else:
        break
    label += 1
    
label_counts.sort()
print(len(label_counts))
for i in label_counts:
    print(i)
    
    
        



            


