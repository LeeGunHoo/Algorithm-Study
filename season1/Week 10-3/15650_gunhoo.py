from itertools import combinations

n, m = map(int, input().split())
num = [i for i in range(1, n + 1)]
nnum = list(combinations(num, m))
nnum.sort()
for i in nnum:
    print(*i)
    # for j in i:
    #     print(j)
