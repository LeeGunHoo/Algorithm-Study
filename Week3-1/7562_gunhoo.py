n = int(input())

def bfs(nx, ny, gx, gy):
    dx = [1, 1, 2, 2, -1, -1, -2, -2]
    dy = [2, -2, 1, -1, 2, -2, 1, -1]
    q = []
    q.append((nx, ny))
    checked[nx][ny] = 1
    while q:
        x, y = q.pop(0)
        if x == gx and y == gy:
            return checked[gx][gy] - 1
        for i in range(8):
            x1 = x + dx[i]
            y1 = y + dy[i]
            if 0 <= x1 < l and 0 <= y1 < l and checked[x1][y1] == 0:
                q.append((x1, y1))
                checked[x1][y1] = checked[x][y] + 1

for _ in range(n):
    l = int(input())
    nx, ny = map(int, input().split())
    gx, gy = map(int, input().split())
    checked = [[0]*l for _ in range(l)]
    ans = bfs(nx, ny, gx, gy)
    print(ans)
