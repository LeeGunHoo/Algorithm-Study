n = int(input())
score = [0]
dp = [0 for _ in range(n+1)]

for _ in range(n):
    score.append(int(input()))

dp[1] = score[1]

for i in range(2, n+1):
    dp[i] = max(dp[i-3] + score[i] + score[i-1], dp[i-2] + score[i])

print(dp[n])

