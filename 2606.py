from collections import deque

number_of_com = int(input())

edge_count = int(input())

edges_temp = [list(map(int, input().split())) for _ in range(edge_count)] 
edges = [[] for _ in range(number_of_com)]
visited = [False for _ in range(number_of_com)]
for edge in edges_temp:
    left, right = edge
    edges[left - 1].append(right)
    edges[right - 1].append(left)
    

def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start - 1] = True
    while len(queue) != 0:
        start = queue.popleft()
        for edge in edges[start - 1]:
            if not visited[edge - 1]:
                visited[edge - 1] = True
                queue.append(edge)
                
    count = 0
    for isVisit in visited:
        if isVisit:
            count += 1
    
    return count - 1

print(bfs(1))
    

    