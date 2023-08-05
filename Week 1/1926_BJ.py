from collections import deque

n, m = map(int, input().split())
picture = []

for _ in range(n):
    picture.append(list(map(int, input().split())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(picture, x, y):
    queue = deque()
    queue.append((x, y))
    picture[x][y] = 0
    cnt = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if picture[nx][ny] == 1:
                picture[nx][ny] = 0
                queue.append((nx, ny))
                cnt += 1
    return cnt

pic_num = []
for i in range(n):
    for j in range(m):
        if picture[i][j] == 1:
            pic_num.append(bfs(picture, i , j))

if len(pic_num) == 0:
    print(len(pic_num))
    print(0)
else:
    print(len(pic_num))
    print(max(pic_num))

