n, m, x, y, k = map(int, input().split())
maps = []
dice = [0] * 6

for _ in range(n):
    i, j = map(int, input().split())
    maps.append([i, j])

order = list(map(int, input().split()))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

dice[0] = maps[x][y]
maps[x][y] = 0

for o in order:
    nx = x + dx[o-1]
    ny = y + dy[o-1]
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        nx = nx - dx[o-1]
        ny = ny - dy[o-1]
        continue
    if o == 1:
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
        dice[2] = maps[nx][ny]
        maps[nx][ny] = 0
    elif o == 2:
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
        dice[3] = maps[nx][ny]
        maps[nx][ny] = 0
    elif o == 3:
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]
        dice[1] = maps[nx][ny]
        maps[nx][ny] = 0
    elif o == 4:
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]
        dice[4] = maps[nx][ny]
        maps[nx][ny] = 0

    print(dice[0])
