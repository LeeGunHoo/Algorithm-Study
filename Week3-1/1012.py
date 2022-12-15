# 지렁이의 최소 마리수?? -> bfs
T = int(input())

def bfs(ground, i, j):
    # bfs -> queue!! check 한 땅은 다시 안가게 0으로!!
    checked = []
    checked.append((i, j))
    ground[i][j] = 0
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    # 다음 확인할 땅이 1이라면 계속 while문 반복
    while checked:
        x, y = checked.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if ground[nx][ny] == 1:
                ground[nx][ny] = 0
                checked.append((nx, ny))
    return

for i in range(T):
    N, M, K = map(int, input().split())
    ground = [[0] * M for _ in range(N)]
    cnt = 0

    for _ in range(K):
        X, Y = map(int, input().split())
        ground[X][Y] = 1

    for i in range(N):
        for j in range(M):
            if ground[i][j] == 1:
                bfs(ground, i, j)
                cnt += 1

    print(cnt)