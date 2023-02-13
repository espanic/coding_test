import sys
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [-1 for i in range(n + 1)]

def find(x):
    if parent[x] < 0:
        return x
    else:
        y = find(parent[x])
        parent[x] = y
        return y
    
def union(x, y):
    x = find(x) # x의 root
    y = find(y) # y의 root
    if x == y:
        return
    if parent[x] < parent[y]:
        parent[x] += parent[y]
        parent[y] = x
    else:
        parent[y] += parent[x]
        parent[x] = y
        
def isAtSameSet(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        print("YES")
    else:
        print("NO")


for _ in range(m):
    flag, x, y = map(int, input().split())
    if flag == 0:
        union(x, y)
    else:
        isAtSameSet(x, y)