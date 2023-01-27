INF = 2000000000

N = int(input())

liquids = list(map(int, input().split()))
liquids.sort()


def find_smallest(i):
    abs_sum = INF
    pair = None
    u = liquids[i]
    
    def search(p, r):
        nonlocal abs_sum
        nonlocal pair
        
        if p > r:
            return
        q = (p + r) // 2
        
        if i != q:
            temp = liquids[q] + u
            if abs(temp) < abs_sum:
                abs_sum = abs(temp)
                pair = liquids[q]
            if temp > 0:
                search(p, q - 1)
            elif temp < 0:
                search(q +1 , r)
            else:
                return
        else:
            search(p, q - 1)
            search(q +1 , r)
            return 
            
    search(0, N - 1)
    
    return abs_sum, pair
        
        
result = []
smallest = INF
pairs = None
for i in range(N):
    
    abs_sum, pair = find_smallest(i)

    if abs_sum < smallest:
        smallest = abs_sum
        pairs = [liquids[i], pair]
        
    
pairs.sort()
print(pairs[0], pairs[1])



