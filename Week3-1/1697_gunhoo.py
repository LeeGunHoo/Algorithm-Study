# 최단 시간이긴 한데 사실상 최단 거리랑 비슷한 의미 아닐까...

N,K = map(int, input().split())
checked = [0 for _ in range(100001)]

def bfs(N):
    q = []
    q.append(N)
    while q:
        x = q.pop(0)
        if x == K:
            return checked[x]
        for i in (x-1, x+1, 2*x):
            if 0 <= i <= 100000 and not checked[i]:
                checked[i] = checked[x] + 1
                q.append(i)

ans = bfs(N)
print(ans)
