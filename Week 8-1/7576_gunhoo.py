# 최소일수 == 최단거리??
# 비슷한 느낌이니 bfs 쓰면 되지 않을까!
# 항상 queue 쓰는데 deque가 좀 더 빠르다고 하니 deque 쓰도록 해봐야겠다.
# 전형적인 bfs 형태로 풀었다. 이제는 뭔가 걍 코드를 외운느낌....

from collections import deque

M, N = map(int, input().split())
house = []

for _ in range(N):
    house.append(list(map(int, input().split())))

ans = 0
q = deque([])
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for i in range(N):
    for j in range(M):
        if house[i][j] == 1:
            q.append([i, j])

def bfs():
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and house[nx][ny] == 0:
                q.append([nx, ny])
                house[nx][ny] = house[x][y] + 1

bfs()

for i in house:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    ans = max(ans, max(i))

print(ans - 1)