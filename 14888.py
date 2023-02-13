from collections import deque

N = int(input())
numbers = deque(list(map(int, input().split())))

operator_num = list(map(int, input().split())) #덧셈, 뺄셈, 곱셈, 나눗셈

prev_val = 0

max_val = - 1000000000
min_val = 1000000000
    
def operation(val1, val2, op, operator_num):
    if operator_num[op]:
        if op == 0:
            new_val = val1 + val2
        elif op == 1:
            new_val = val1 - val2
        elif op == 2:
            new_val = val1 * val2
        else:
            if val1 >= 0:
                sign = 1
            else:
                sign = - 1

            new_val = abs(val1) // val2 * sign
        return new_val
    return None

    
def backtracking(numbers, operator_num):
    global max_val
    global min_val
    if len(numbers) == 1:
        max_val = max(max_val, numbers[0])
        min_val = min(min_val, numbers[0])
    else:
        prev_val = numbers.popleft()
        val = numbers.popleft()
        for i in range(4):
            new_val = operation(prev_val, val, i, operator_num)
            if new_val is not None:
                operator_num[i] -= 1
                numbers.appendleft(new_val)
                backtracking(numbers, operator_num)
                operator_num[i] += 1
                numbers.popleft()
        numbers.appendleft(val)
        numbers.appendleft(prev_val)
        
            
backtracking(numbers, operator_num)       
print(max_val)
print(min_val)
    
    
    
    

