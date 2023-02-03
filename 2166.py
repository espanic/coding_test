from math import sin, pi

N  = int(input())
vertices = [list(map(int, input().split())) for _ in range(N)]

res = 0


for i in range(N - 1):
    res += vertices[i][0] * vertices[i + 1][1]

res += vertices[N - 1][0] * vertices[0][1]

for i in range(N - 1):
    res -= vertices[i][1] * vertices[i + 1][0]
res -= vertices[N-1][1] * vertices[0][0]

print(round(abs(res) / 2, 2))