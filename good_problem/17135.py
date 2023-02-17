from itertools import combinations

N, M, D = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]


def is_not_overflow(u):
    x, y = u
    if x >= 0 and x < N and y >= 0 and y < M:
        return True
    return False

def find_attackable_area(loc):
    x = N
    for d in range(1, D + 1):
        for i in range(1, d):
            newx = x - i
            newy = N - d + loc - newx
            if is_not_overflow([newx, newy]):
                yield newx, newy
        
        newx = x -d
        newy = loc
        if is_not_overflow([newx, newy]):
            yield newx, newy
        
        for i in range(d - 1, 0, -1):
            newx = x - i
            newy = newx - N +d + loc
            if is_not_overflow([newx, newy]):
                yield newx, newy
    
    
    
answer = 0

for arrow_locs in combinations(range(M), 3):
    cnt = 0
    new_board = [row.copy() for row in board]

    while True:
        enemies = []
        for i in range(N):
            for j in range(M):
                if new_board[i][j] == 1:
                    enemies.append([i,j])
        if len(enemies) == 0:
            break
                    
                    
        deleted_enemy = set()

        for loc in arrow_locs:
            for x,y in find_attackable_area(loc):
                if new_board[x][y] == 1:
                    deleted_enemy.add((x,y))
                    break
        
        cnt += len(deleted_enemy)
        
        for enemy in enemies:
            x, y = enemy
            new_board[x][y] = 0
        for enemy in enemies:
            x, y = enemy
            if (x, y) not in deleted_enemy:
                if is_not_overflow([x + 1,y]):

                    new_board[x+1][y] = 1
            
                

    # print(arrow_locs,cnt)
    answer = max(cnt, answer)
print(answer)
         
        
    

        
