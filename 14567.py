N, M = map(int, input().split())
edges = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    edges[a-1].append(b- 1)
    

    
def topological_sort():
    visited = [False for _ in range(N)]
    topo_list = []
    
    def dfs_ts(u):
        nonlocal visited
        visited[u] = True
        for v in edges[u]:
            if not visited[v]:
                dfs_ts(v)
        topo_list.append(u)

    for u in range(N):
        if not visited[u]:
            dfs_ts(u)
    
    topo_list.reverse()
    
    ans = [0 for _ in range(N)]
    for u in topo_list:
        ans[u] = max(ans[u], 1)
        for v in edges[u]:
            ans[v] = max(ans[v], ans[u] + 1 )
    
    
            
    print(" ".join(map(str, ans)))

topological_sort()