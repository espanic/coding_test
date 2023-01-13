n, k = list(map(int, input().split()))
coins = [int(input()) for _ in range(n)]
coins.sort()

dp = [1] + [0] * k

for coin in coins:
    for i in range(1, k + 1):
        if i - coin >= 0:
            dp[i] += dp[ i - coin] 

print(dp[-1])