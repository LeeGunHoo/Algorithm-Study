dp = []
n = int(input())

for i in range(n):
    dp += [list(map(int, input().split()))]

for i in range(n-2, -1, -1):
    for j in range(len(dp[i])):
        dp[i][j] += max(dp[i+1][j:j+2])

print(dp[0][0])