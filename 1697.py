from collections import deque
import sys
input = sys.stdin.readline
N, K = list(map(int, input().split()))


def next_point(x):
    return x - 1, x + 1, 2 * x



visited = [False] * 100001
queue = deque()
x = N

visited[x] = True

queue.append((x, 0))

def dfs():
    while queue:
        u, sec = queue.popleft()
        if u == K:
            return sec
        for neighbor in next_point(u):
            if neighbor>= 0 and neighbor <= 100000 and not visited[neighbor]:
                visited[neighbor] = True
                queue.append((neighbor, sec + 1))

print(dfs())
            
    

