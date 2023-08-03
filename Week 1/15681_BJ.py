import sys

si = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
N, R, Q = map(int, si().split())

arr = [[] for i in range(N + 1)]
cnt = [1] * (N + 1)
for i in range(N - 1):
    x, y = map(int, si().split())
    arr[x].append(y)
    arr[y].append(x)


def dfs(x, par):
    for i in arr[x]:
        if i == par: continue
        dfs(i, x)
        cnt[x] += cnt[i]


dfs(R, -1)
for i in range(Q):
    print(cnt[int(si())])