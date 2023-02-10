import sys
input = sys.stdin.readline
board = []
emptys = []
for i in range(9):
    row = list(map(int, input().split()))
    for j in range(9):
        if not row[j]:
            emptys.append([i,j])
    board.append(row)
    
def check_available_number(u):
    x, y = u
    p, q = (x // 3) * 3, (y // 3) * 3
    num_check = [False for _ in range(9)]
  
    for val in board[x]:
        if val != 0:
            num_check[val - 1] = True
            
    for j in range(9):
        if board[j][y] != 0:
            num_check[board[j][y] - 1] = True
            
    for i in range(p, p + 3):
        for j in range(q, q + 3):
            if board[i][j] != 0:
                num_check[board[i][j] - 1] = True
            
    result  = []
    for i, check in enumerate(num_check):
        if not check:
            result.append(i + 1)
    return result
            
            
answer = None
def solve_stoku(ind):
    if ind < len(emptys):
        empty_loc = emptys[ind]
        x, y = empty_loc
        available_number = check_available_number([x, y])
        for num in available_number:
            board[x][y] = num
            already_find = solve_stoku(ind + 1)
            if already_find == True:
                return True
            board[x][y] = 0
    else:
        print_board()
        return True
    
def print_board():
    for row in board:
        print(" ".join(map(str, row)))
        
solve_stoku(0)

        