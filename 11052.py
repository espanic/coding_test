N = int(input())
P =  list(map(int, input().split()))

records = [0]

for i in range(1, N + 1):
    max_val = 0
    
    for j, record in enumerate(records):
        val = record + P[i - j - 1]
        if max_val < val:
            max_val = val
    records.append(max_val)
    
print(records[-1])