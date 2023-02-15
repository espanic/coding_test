N = int(input())

records = [1, 0, 3, 0, 11, 0,]


for i in range(4, N + 1):
    if i % 2 != 0:
        records.append(0)
    else:
        records.append(records[i - 2] * 3 +  sum(records[:i -3]) * 2 +8)

print(records[-1])

