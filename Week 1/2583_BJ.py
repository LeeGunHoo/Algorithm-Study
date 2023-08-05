from collections import deque

m, n, k = map(int, input().split())
square = [[0] * n for _ in range(m)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            square[i][j] = 1

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    cnt = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if square[nx][ny] == 0:
                square[nx][ny] = 1
                queue.append((nx, ny))
                cnt += 1         
    return cnt

square_num = []

for i in range(m):
    for j in range(n):
        if square[i][j] == 0:
            square[i][j] += 1
            square_num.append(bfs(i, j))

print(len(square_num))
print(*sorted(square_num))
