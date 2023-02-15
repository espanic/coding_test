N = int(input())
buildings = list(map(int, input().split()))
# buildings = [[i + 1, building] for i, building in enumerate(buildings)]


def compute_gradient(a, b):
    a_x, a_y = a
    b_x, b_y = b
    return (b_y - a_y) / (b_x - a_x)

answer = 0

for x, y in enumerate(buildings):
    
    gradient = 1000000001
    cnt = 0
    for x2 in range(x - 1, - 1, -1):
        y2 = buildings[x2]
        new_gradient = compute_gradient((x, y), (x2, y2))
        if new_gradient < gradient:
            cnt += 1
            gradient = new_gradient
        
    gradient = - 1000000001
        
    for x2 in range(x + 1, N):
        y2 = buildings[x2]
        new_gradient = compute_gradient((x, y), (x2, y2))
        if new_gradient > gradient:
            cnt += 1
            gradient = new_gradient  
            
    answer = max(answer, cnt)
        
print(answer)



