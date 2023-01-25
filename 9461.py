import sys
input = sys.stdin.readline

records = [0, 1, 1, 1, 2]

def solve(n):
    i = len(records)
    if i > n:
        return records[n]
    for j in range(i, n + 1):
        records.append(records[j-1] + records[j - 5])
    return records[n]
    

T = int(input())


result = []
for _ in range(T):
    n = int(input())
    result.append(solve(n))
    
    
for r in result:
    print(r)