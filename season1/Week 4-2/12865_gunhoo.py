n, k = map(int, input().split())
bag = []
dp = [0 for _ in range(k+1)]

for _ in range(n):
    w, v = map(int, input().split())
    bag.append((w, v))

for i in range(len(bag)):
    for j in range(bag[i][0], k+1):
        dp[j] = max(dp[j], dp[i-j] + bag[i][1])
        print(dp)
print(dp[k])