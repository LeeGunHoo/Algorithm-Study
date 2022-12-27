n, k = map(int, input().split())
coin = []

for _ in range(n):
    coin.append(int(input()))
dp = [10001 for _ in range(k+1)]
dp[0] = 0

coin.sort(reverse=True)

for i in coin:
    for j in range(i, k+1):
        dp[j] = min(dp[j], dp[j-i] + 1)

if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])