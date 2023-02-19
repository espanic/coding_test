from collections import deque

operators = ('+', '-', '/', '*')
def isOperator(a):
    return a in operators

N = int(input())

temp = list(input())
values = [int(input()) for _ in range(N)]
def get_val(a):
    return values[ord(a) - 65]

def perform_operation(a, b, operator):
    if operator == '+':
        return a+b
    elif operator == '-':
        return a- b
    elif operator == '/':
        return a / b
    else:
        return a * b

equation = deque()
for i in temp:
    if not isOperator(i):
        equation.append(get_val(i))
    else:
        equation.append(i)
del temp

buffer = []

while len(equation) > 1:
    while not isOperator(equation[0]):
        buffer.append(equation.popleft())
        
    operator = equation.popleft()
    val2 = buffer.pop()
    val1 = buffer.pop()
    res = perform_operation(val1, val2, operator)
    equation.appendleft(res)
    
    
    
print(f"{equation[-1]:.2f}")


