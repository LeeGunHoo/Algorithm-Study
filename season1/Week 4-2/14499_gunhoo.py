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
    if o == 1:
        if y+1 >= m:
            dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]
            dice[2] = maps[x][y+1]
            dice[]
    elif o == 2:

    elif o == 3:

    elif o == 4:

