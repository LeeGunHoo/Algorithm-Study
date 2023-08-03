from collections import deque

n, m, v = list(map(int, input().split()))

l = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    i, j = map(int, input().split())
    l[i][j] = 1
    l[j][i] = 1

visited1 = [0] * (n + 1)
visited2 = [0] * (n + 1)

def dfs(v):
    visited1[v] = 1
    print(v, end=' ')
    for i in range(1, n + 1):
        if l[v][i] == 1 and visited1[i] == 0:
            dfs(i)

def bfs(v):
    q = deque([v])
    visited2[v] = 1

    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in range(1, n + 1):
            if l[v][i] == 1 and visited2[i] == 0:
                q.append(i)
                visited2[i] = 1

dfs(v)
print()
bfs(v)