N =int(input())

count  = 0
col_check = [False] * N
left_down = [False] * (2 * N - 1)
right_down = [False] * (2 * N - 1)
def recursive(depth):
    global count 
    if depth == N:
        count += 1
        return
    
    for j in range(N):
        # if not canAttackFaster(depth, j):
        if  not col_check[j] and not left_down[depth - j + N -1] and not right_down[depth +j]:
            col_check[j] = left_down[depth - j + N - 1] = right_down[depth + j] = True
            recursive(depth + 1)
            col_check[j] = left_down[depth - j + N - 1] = right_down[depth +j] = False



def canAttackFaster(i, j):
    if  col_check[j] or left_down[i - j + N -1] or right_down[i +j]:
        return True
    return False
    


recursive(0)
print(count)
    
    

