# n = int(input())
# dp = [0]
# wine = [0]
# for i in range(1, n+1):
#     wine.append(int(input()))
#     if i == 1:
#         dp.append(wine[i])
#     elif i == 2:
#         dp.append(dp[1] + wine[i])
#     else:
#         dp.append(max(dp[i-1], dp[i-2] + wine[i], dp[i-3] + wine[i-1] + wine[i]))
# print(dp[n])

n = int(input())
dp = [0]*(n+1)
wine = [0]
for i in range(1, n+1):
    wine.append(int(input()))
    if i == 1:
        dp[i] = wine[i]
    elif i == 2:
        dp[i] = dp[1] + wine[i]
    else:
        dp[i] = max(dp[i-1], dp[i-2] + wine[i], dp[i-3] + wine[i-1] + wine[i])
print(dp[n])

