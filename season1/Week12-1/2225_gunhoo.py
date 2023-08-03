from itertools import combinations_with_replacement
from math import comb
# 중복 조합. k개의 자리에 n개의 1을 넣는다고 생각하자.
n, k = map(int, input().split())

# print(len(combinations_with_replacement(num, n)) % 1000000000)
print(comb(k+n-1, n) % 1000000000)

# n, k = map(int,input().split())
# l = [1 for _ in range(n+1)]
# for i in range(k-1):
#     for j in range(1,n+1):
#         l[j] += l[j-1]
# print(l[-1] % 1000000000)