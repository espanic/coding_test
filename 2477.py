import sys
from enum import Enum

# class Direction(Enum):
#     east = 1
#     west = 2
#     south = 3
#     north = 4
    
# class Edge:
#     def __init__(self, dir, length, inner = False):
#         self.dir = dir
#         self.length = length
#         self.inner = inner

input = sys.stdin.readline
number_of_chame = int(input())



edges = []
dir_appear_twice = [True for _ in range(4)]
for i in range(6):
    dir,length = map(int, input().split())
    dir_appear_twice[dir - 1] = not dir_appear_twice[dir - 1]
    edges.append((dir - 1, length))
    
dir1, dir2 = [i for i in range(4) if dir_appear_twice[i]]



def get_inner_index(loc_pattern):
    if loc_pattern == [0, 1,2,3]:
        return 1, 2
    if loc_pattern == [1,2,3,4]:
        return 2, 3
    if loc_pattern == [2,3,4,5]:
        return 3, 4
    if loc_pattern == [0,3,4,5]:
        return 4, 5
    if loc_pattern == [0,1, 4, 5]:
        return 0, 5
    if loc_pattern == [0,1,2,5]:
        return 0, 1

loc_pattern = []
big_length = []
for i, edge in enumerate(edges):
    if edge[0] == dir1 or edge[0] == dir2:
        loc_pattern.append(i)
    else:
        big_length.append(edge[1])


inner_index1, inner_index2 = get_inner_index(loc_pattern)

small_area = edges[inner_index1][1] *  edges[inner_index2][1]

big_area = big_length[0] * big_length[1]

print((big_area - small_area) * number_of_chame)





        
    
    


    
