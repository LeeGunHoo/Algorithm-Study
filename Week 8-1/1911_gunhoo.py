N, L = map(int, input().split())
l = []

# 웅덩이를 일단 순서대로 정렬해주자
for _ in range(N):
    l.append(tuple(map(int, input().split())))
l.sort()

# 널빤지 길이만큼 자르고, 남으면 그곳을 시작점으로 설정하면 된다.
ans = 0
start = 0
for left, right in l:
    start = max(left, start)
    pool = right - start
    if (pool/L) == (pool//L):
        cnt = (pool // L)
    else:
        cnt = (pool // L) + 1
    ans += cnt
    start += cnt * L

print(ans)