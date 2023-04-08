# 모든 가능한 조합을 전부 찾은 뒤, 집과 치킨집의 거리를 전부 계산한다.
# 반복문을 집의 개수만큼 돌려주고, 반복문 1회마다 해당 조합에서 나올 수 있는 최솟값을 더해준다.
# 이 과정을 모든 조합에 대해 실행하고, 또 이에 대한 최솟값을 저장해 빼낸다.
# 궁금증 : 백트래킹이란 어떤 경우를 타다가 아니면 다시 빠져야하는데 이건 조합 전체를 보는 거라 사실상 그냥 구현이다..

from itertools import combinations

n, m = map(int, input().split())
city = list(list(map(int, input().split())) for _ in range(n))

house = []
chicken = []
ans = float('inf')

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append((i, j))
        elif city[i][j] == 2:
            chicken.append((i, j))

for com in combinations(chicken, m):
    m = 0
    for i in range(len(house)):
        m += min(abs(house[i][0] - com[j][0]) + abs(house[i][1] - com[j][1]) for j in range(len(com)))
    ans = min(m, ans)

print(ans)
