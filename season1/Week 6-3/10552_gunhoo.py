n, m, p = map(int, input().split())
s = [0] * (m + 1)
cnt = 0

for i in range(n):
    a, b = map(int, input().split())
    if not s[b]:
        s[b] = a

for i in range(m):
    if not s[p]:
        print(cnt)
        exit()
    cnt += 1
    p = s[p]

print(-1)