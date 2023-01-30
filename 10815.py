N = int(input())
have = list(map(int, input().split()))
have.sort()
M = int(input())
guess = list(map(int, input().split()))



def find(n, p, r):
    if p > r:
        return 0
    q = (p + r) // 2
    
    if have[q] == n:
        return 1
    elif have[q] > n:
        return find(n, p, q - 1)
    else:
        return find(n, q +1, r)
    
result  = []

for n in guess:
    result.append(find(n, 0, N - 1))

for i, res in enumerate(result):
    if i == len(result) - 1:
        print(res)
    else:
        print(res, end = " ")
        
    