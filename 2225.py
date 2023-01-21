
###
# f(n, k) 를 0~N의 k개의 수로 합이 n을 만드는 경우의 수일 때
# f(n, k) = f(n, k - 1) + sum^{n-1}_{i=0}f(i, k - 1)

###

N, K = list(map(int, input().split()))


records = [[1] * K]

for sum in range(1 ,  N + 1):
    record = [1]
    add_val = 0
    for j in range(1, K ):
        add_val = record[j - 1]
        for i in range(sum):
            add_val += records[i][j - 1]
        record.append(add_val)
    records.append(record)
    
print(records[-1][-1] % 1000000000)