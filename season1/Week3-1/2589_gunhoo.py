n, m = map(int, input().split())
maps = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
checked = []
ans = 0
for _ in range(n):
    maps.append(list(input()))

def bfs(i, j):
    global ans
    q = []
    q.append((i, j))
    while q:
        x, y = q.pop(0)
        checked.append((x, y))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if maps[nx][ny] == "W":
                continue
            if (nx, ny) not in checked and maps[nx][ny] == "L":
                q.append((nx, ny))
                l[nx][ny] = l[x][y] + 1
                ans = max(ans, l[nx][ny])
    return ans

for i in range(n):
    for j in range(m):
        if maps[i][j] == "L":
            l = [[0] * m for _ in range(n)]
            res = bfs(i, j)

print(res+1)

