import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000)


    

    
if __name__ == '__main__':
    T = int(input())
    
    
    def neighbors(u):
        x, y = u
        if x - 1 >=0:
            yield x - 1, y
        if y - 1 >= 0:
            yield x, y - 1
        if x + 1 < N:
            yield x + 1, y
        if y + 1 < M:
            yield x , y + 1
    
    
    def find_left_cabbage(field):
        for i in range(N):
            for j in range(M):
                if field[i][j]:
                    return i, j
        return None
            
    def dfs(u, field):
        x, y = u
        field[x][y] = 0
        for neighbor in neighbors(u):
            if field[neighbor[0]][neighbor[1]]:
                dfs(neighbor, field)
    
    for _ in range(T):
        M, N, K = map(int, input().split())
        field = [[0 for _ in range(M)] for _ in range(N)]
        for _ in range(K):
            y, x  = map(int, input().split())
            field[x][y] = 1
        

        count = 0
        while True:
            u = find_left_cabbage(field)
            if u is None:
                break        
            dfs(u, field)
            count += 1
        
        print(count)
    