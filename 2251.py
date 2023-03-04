A_cap, B_cap, C_cap = map(int, input().split())
visited = [[[False for _ in range(C_cap + 1)]  for _ in range(C_cap + 1)] for _ in range(C_cap+1)]
record = []



def pour_x_to_z(x, y, z,z_cap):
    if x == 0 or z == z_cap:
        return None
    newx = max(0, x - (z_cap - z))
    newz = z + (x - newx)
    return [newx, y, newz]
    
    
def dfs(abc, depth):
    a,b,c = abc
    if visited[a][b][c]:
        return
    visited[a][b][c] = True
    if c == C_cap and depth != 1:
        return
    if a== 0:
        record.append(c)
    
    result = pour_x_to_z(a, b, c, C_cap)
    if result is not None:
        dfs(result, depth + 1)
        
    result = pour_x_to_z(c, b, a, A_cap)
    if result is not None:
        dfs([result[2], result[1], result[0]], depth + 1)
        
    result = pour_x_to_z(b, a, c, C_cap)
    if result is not None:
        dfs([result[1], result[0], result[2]], depth+1)
        
    result = pour_x_to_z(c, a, b, B_cap)
    if result is not None:
        dfs([result[1], result[2], result[0]], depth + 1)
        
    result = pour_x_to_z(a, c, b, B_cap)
    if result is not None:
        dfs([result[0], result[2], result[1]], depth + 1)
        
    result = pour_x_to_z(c, b, a, A_cap)
    if result is not None:
        dfs([result[2], result[1], result[0]], depth +1)
    

dfs([0,0,C_cap],1)

        
record = list(set(record))
record.sort()
print(" ".join(map(str, record)))

    
    
    





