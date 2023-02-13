import sys
input = sys.stdin.readline
N = int(input())
M = int(input())

parent = [-1 for _ in range(N)]

def find(x):
    if parent[x] < 0:
        return x
    else:
        y = find(parent[x])
        parent[x] = y
        return y
    
def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x == root_y:
        return 
    if parent[root_x] < parent[root_y]:
        parent[root_x] += parent[root_y]
        parent[root_y] = root_x
    else:
        parent[root_y] += parent[root_x]
        parent[root_x] = root_y


for i in range(N):
    command = list(map(int, input().split()))
    for j, val in enumerate(command):
        if val == 1:
            union(i, j)
            
answer = "YES"      
trip_plan = list(map(int, input().split()))
if trip_plan:
    trip_root = find(trip_plan[0] - 1)

    for i in range(1, len(trip_plan)):
        if trip_root != find(trip_plan[i] - 1):
            answer = "NO"
            break
print(answer)
        