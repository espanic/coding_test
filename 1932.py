n = int(input())

triangle = [list(map(int,input().split())) for _ in range(n)]

max_sums = []

max_sums.append(triangle[0])



for i in range(1, n):
    max_sum_level = []
    value_level = triangle[i]
    for j in range(i + 1):
        if j == 0:
            max_parent = max_sums[i-1][j]
        elif j == i:
            max_parent = max_sums[i-1][j - 1]
        else:
            max_parent = max(max_sums[i - 1][j-1], max_sums[i-1][j])
        max_sum_level.append(max_parent + value_level[j])
    max_sums.append(max_sum_level)

print(max(max_sums[n-1]))
            
        
        