n = int(input())
arr = list(map(int, input().split()))

dp = [[arr[i]] for i in range(n)]
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j] and len(dp[i]) < len(dp[j])+1:
            dp[i] = dp[j] + [arr[i]]

ans = max(dp, key=len)
print(len(ans))
print(*ans)