n, m = map(int, input().split())
cloud = [[0, n-1], [0, n-2], [1, n-1], [1, n-2]]
basket = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]
bug_dx = [1, 1, -1, -1]
bug_dy = [1, -1, 1, -1]

# m번의 이동을 시키자.
for _ in range(m):
  d, s = map(int, input().split())
  rained = [[0]*n for _ in range(n)]

  # 이동한 위치에 비내리기
  for x, y in cloud:
    x, y = (x + s * dx[d-1]) % n, (y + s * dy[d - 1]) % n
    rained[y][x] = 1

  tmp = []

  for i in range(n):
    for j in range(n):
      # 5번 조건. 새 배열에다가 결과 정보를 저장.
      if basket[i][j] >= 2 and rained[i][j] == 0:
        basket[i][j] -= 2
        tmp.append([j,i])
      # 비내려서 1증가시키고, 물복사 버그 실행
      elif rained[i][j] > 0 :
        cnt = 0
        for k in range(4):
          nx, ny = j + bug_dx[k], i + bug_dy[k]
          # 4번 조건.
          if -1 < nx < n and -1 < ny < n and (basket[ny][nx] > 0 or rained[ny][nx] > 0 or [nx, ny] in tmp):
            cnt += 1
        basket[i][j] += cnt + rained[i][j]

  cloud = tmp

print(sum(map(sum, basket)))