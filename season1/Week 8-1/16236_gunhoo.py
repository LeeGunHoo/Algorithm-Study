# 구현 파트에 있었던 것 같은데, 그래프 문제 같다.
# 조건 중에 지나야하는 칸의 개수가 최솟값이라 했으므로 bfs 유력
# 코드는 7576이랑 비슷할 것 같다.
from collections import deque

N = int(input())
space = list(list(map(int, input().split())) for _ in range(N))

b_shark = 2
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 일단 시작 지점부터 찾아주자
for i in range(N):
    for j in range(N):
        if space[i][j] == 9:
            x, y = i, j
            space[i][j] = 0

# 최단거리 bfs
def bfs():
    q = deque([[x, y]])
    checked = [[-1] * N for _ in range(N)]
    checked[x][y] = 0

    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < N and 0 <= ny < N and b_shark >= space[nx][ny] and checked[nx][ny] == -1:
                q.append([nx, ny])
                checked[nx][ny] = checked[cx][cy] + 1

    return checked

# 아아아아.... 모르겠다.......뭐 어쩌라는거임