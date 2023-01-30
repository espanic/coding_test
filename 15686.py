import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
city_info = [list(map(int, input().split())) for _ in range(N)]
houses = []
chickens = {}
chickens = []
for i in range(N):
    for j in range(N):
        if city_info[i][j] == 1:
            houses.append([i, j])
        elif city_info[i][j] == 2:
            chickens.append((i, j))      
            
        
def get_distance(house, col):
    min_dist = int(1e9)
    x, y = house
    for chicken in col:
        i, j = chicken
        val = abs(x - i) + abs(y - j)
        if val < min_dist:
            min_dist = val
    return min_dist
    

    


result = int(1e9)
for col in combinations(chickens, M):

        
    temp = 0
    
    for house in houses:
        v = get_distance(house, col)
        # print(v)
        temp += v
        
    if temp < result:
        result = temp


    

print(result)
    


