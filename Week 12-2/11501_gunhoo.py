# 내 왼쪽에 있는 것 중 나보다 작은 값만 찾으면 된다.

t = int(input())

for _ in range(t):
    n = int(input())
    price = list(map(int, input().split()))
    ans, tmp = 0, 0
    for i in range(n-1, -1, -1):
        if price[i] > tmp:
            tmp = price[i]
        else:
            ans += tmp - price[i]
    print(ans)