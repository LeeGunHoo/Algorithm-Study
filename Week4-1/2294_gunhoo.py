# 메모제이션을 계속 생각하자.
# 최적인 답에 대해서는 여전히 애매...
# 그리고 이러면 계속 배열을 길이를 늘려야하나..? 편하긴 한데 다른 방법이 떠오르질 않는다
# 그리고 런타임 에러...
n, k = map(int, input().split())
coin = []
dp = [0 for _ in range(k + 1)]

for _ in range(n):
    coin.append(int(input()))

for price in range(1, k + 1):
    a = []
    for value in coin:
        if dp[price - value] != 'none' and value <= price:
            a.append(dp[price - value])
    if a:
        dp[price] = min(a) + 1
    else:
        dp[price] = 'none'

print(dp[k])