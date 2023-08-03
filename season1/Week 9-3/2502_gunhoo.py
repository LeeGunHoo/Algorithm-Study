import sys

d, k = map(int, input().split())

dp = [1, 1] + [0 for _ in range(d-2)]

while True:
    fibo = int(((((1 + 5 ** 0.5) / 2) ** (d-2)) * (dp[0] + (((1 + 5 ** 0.5) / 2) * dp[1])) - (((1 - 5 ** 0.5) / 2) ** (d-2)) * (dp[0] + (((1 - 5 ** 0.5) / 2) * dp[1]))) / (5 ** 0.5))
    print((dp[0],dp[1]))
    print(fibo)
    if fibo == k:
        print(dp[0])
        print(dp[1])
        sys.exit(0)
    elif fibo > k:
        dp[0] += 1
        dp[1] = dp[0]
    else:
        dp[1] += 1

