# 저번에 봤던 rotate를 사용할 수 있을 것 같다. rotate는 deque에서만 사용한다.
# 나머지는 문제에 적혀있는 단계 설명을 옮겨적으면 될 듯.  근데 실패... 퍼센티지가 안올라감.
from collections import deque

n, k = map(int, input().split())
a = deque(list(map(int, input().split())))
r = deque([0 for _ in range(n)])
cnt = 0
while True:
    # 1번 : 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
    a.rotate(1)
    r.rotate(1)
    r[-1] = 0
    # 2번 : 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
    # 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
    if 1 in r:
        for i in range(n-2, -1, -1):
            if r[i] == 1 and r[i + 1] != 1 and a[i + 1] >= 1:
                r[i+1] = 1
                r[i] = 0
                a[i+1] -= 1
                r[-1] = 0
    # 3번 : 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
    if a[0] >= 1 and r[0] == 0:
        r[0] = 1
        a[0] -= 1
    cnt += 1
    # 4번 : 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.
    if a.count(0) >= k:
        break
print(cnt)