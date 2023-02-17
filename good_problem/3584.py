T = int(input())
import sys

def get_level(vertices, v):
    level = 0
    while v!= vertices[v]:
        v = vertices[v]
        level += 1
    return level

def level_up(vertices, v, levelup):
    for _ in range(levelup):
        v = vertices[v]
    return v



for _ in range(T):
    N = int(input())

    vertices = [i for i in range(N)]

    for _ in range(N-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        vertices[b] = a

    v1, v2 = map(int, input().split())
    v1 -= 1
    v2 -= 1
    
    v1_level = get_level(vertices,v1)
    v2_level = get_level(vertices, v2)
    
    if v1_level < v2_level:
        v2 = level_up(vertices, v2, v2_level - v1_level)
    else:
        v1 = level_up(vertices, v1, v1_level - v2_level)
        
    while v1 != v2:
        v1 = vertices[v1]
        v2 = vertices[v2]
    print(v1 + 1)