import sys
input = sys.stdin.readline
N = int(input())
visited = [False for i in range(N)]
edges = [[] for _ in range(N)]


for _ in range(N):
    arr = list(map(int, input().split()))
    n = len(arr) // 2 - 1
    
    i = 1
    for i in range(1, len(arr) - 2, 2):
        x, y = arr[i], arr[i+1]
        edges[arr[0] - 1].append((x - 1, y))




def dfs(u, r):
    max_branch = 0
    visited[u] = True
    
    # branches = [r]
    max_diameter = 0
    
    # max1 = r
    # max2 = r
    branches = [r]
    
    for v, w in edges[u]:
        if not visited[v]:
            branch, d = dfs(v, w)
            max_diameter = max(d, max_diameter)
            
            # max1, max2 = get_2max(max1, max2, branch)
            branches.append(branch)
            # print(f"for  {u} to {v} dfs value is {branch}")
            max_branch = max(branch, max_branch)
            
    if len(branches) == 1:
        max_diameter = max(max_diameter, branches[0])
    else:
        branches.sort(reverse=True)
        max_diameter = max(max_diameter, branches[0] + branches[1])
    # print(max1+max2, max_diameter)
    # max_diameter = max(max1 +max2, max_diameter)
    return  r + max_branch, max_diameter

def get_2max(max1, max2, val):
    if val > max2:
        if val > max1:
            temp = max1
            max1 = val
            max2 = temp
        elif val < max1:
            max2 = val
    
    return max1, max2


r, d = dfs(0,0)
print(max(r, d))