from functools import cmp_to_key

N =int(input())

points = [list(map(int, input().split())) for _ in range(N)]

def comparable(p1, p2):
    if p1[0] < p2[0]:
        return 1
    if p1[0] > p2[0]:
        return -1
    else:
        if p1[1] < p2[1]:
            return 1
        elif p1[1] == p2[1]:
            return 0
        else:
            return -1


points.sort()  

for point in points:
    print(f"{point[0]} {point[1]}")