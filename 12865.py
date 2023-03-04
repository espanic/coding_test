N, K = map(int, input().split())
things =[]

for _ in range(N):
    w, v = map(int, input().split())
    things.append((w,v))
    

 
dp = [[0 for _ in range(K+1)]]

for i in range(1, N+1):
    new_row = []
    item = things[i - 1]
    for j in range(K+1):
        new_value = max(dp[i-1][j], dp[i-1][j-item[0]] + item[1]) if item[0] <= j else dp[i-1][j]
        new_row.append(new_value)
    dp.append(new_row)
        
print(dp[-1][-1])


        
    