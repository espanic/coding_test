import heapq

T = int(input())
INF = 1e9

for _ in range(T):
    K = int(input())
    files = list(map(int, input().split()))
    n =len(files)


    records = []
    sums_records = []
    records.append(files)
    sums_records.append(files)
    i = 1
    while i < n:
        i += 1
        new_layer = []
        new_sum = []
        for j in range(n - i + 1):
            # g(j, j + i)를 계산!
            val = INF
            for k in range(j, j + i - 1):
                temp = records[k - j][j] + records[j + i - k - 2][k +1]
                val = min(val, temp)
                
            s = sums_records[0][j] + sums_records[i - 2][j+1]
            new_sum.append(s)
            new_layer.append(val + s)
        
        # sum for j: j + i
        records.append(new_layer)
        sums_records.append(new_sum)

    print(records[-1][-1] - sums_records[-1][-1])

        
    
    
    