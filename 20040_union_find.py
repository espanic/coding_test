n, m =map(int, input().split())
parent = [-1 for _ in range(n)]

def find(x):
    if parent[x] < 0:
        return x
    y = find(parent[x])
    parent[x] = y
    return y

def union(x, y):
    r_x = find(x)
    r_y = find(y)
    if r_x == r_y:
        return True
    if parent[r_x] < parent[r_y]:
        parent[r_x] += parent[r_y]
        parent[r_y] = r_x
    else:
        parent[r_y] += parent[r_x]
        parent[r_x] = r_y
    return False

answer = 0
for i in range(m):
    a, b = map(int, input().split())
    res = union(a,b)
    if res:
        answer = i + 1
        break
for _ in range(i+1, m):
    input()
print(answer)