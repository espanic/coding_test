from collections import deque
T = int(input())

def perform_order(p, q):
    isReverse = False
    try:
        for order in p:
            if order == 'R':
                isReverse = not isReverse
            else:
                if isReverse:
                    q.pop()
                else:
                    q.popleft()
                
        if isReverse:
            q.reverse()
        result = "[" +  ",".join(map(str, q)) + "]"
    except:
        result = "error"
    return result
    
    
for _ in range(T):
    p = list(input())
    n = int(input())
    
    raw = input()
    if n == 0:
        arr = []
    else:
        arr = list(map(int, raw[1:-1].split(',')))
    q = deque(arr)
    result = perform_order(p, q)
    
    print(result)
    
    

    
