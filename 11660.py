import sys
input = sys.stdin.readline

N, M = map(int, input().split())


board = [list(map(int, input().split())) for _ in range(N)]

psum = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i > 0:
            if j > 0:
                psum[i][j] = psum[i-1][j] + psum[i][j-1] - psum[i-1][j-1] + board[i][j]
            else:
                psum[i][j] = psum[i-1][j] + board[i][j]
        else:
            if j > 0:
                psum[i][j] = psum[i][j-1] + board[i][j]
            else:
                psum[i][j] = board[i][j]


def get_psum(x,y):
    if x>=0 and y>=0:
        return psum[x][y]
    return 0

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1
    answer = get_psum(x2, y2) - get_psum(x2, y1-1) - get_psum(x1-1, y2) + get_psum(x1-1, y1-1)
    print(answer)
    
    