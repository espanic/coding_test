import sys
input = sys.stdin.readline

T = int(input())


def swapping(points):
    points.sort(key = lambda x: (x[0], -x[1]),reverse = True)
    answer = 0
    buffer = []
    while points:
        point = points.pop()
        for i in range(len(buffer)):
            if buffer[i][1] < point[1]:
                break
            answer += 1
        buffer.append(point)
        buffer.sort(key = lambda x: x[1], reverse=True)
    return answer
            

for _ in range(T):
    n = int(input())
    points = [list(map(int, input().split())) for _ in range(n)]
    print(swapping(points))