# eval 함수의 활용을 고민하며 두 가지 풀이로 풀어보았다.
from itertools import permutations

n = int(input())
a = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
ans = []

# 일단 사칙 연산 가능한 경우 전부다 순열 전개
for s in set(permutations('+' * add + '-' * sub + '*' * mul + '/' * div)):
    r = a[0]
    line = str(a[0])

    # Answer1. 딕셔너리를 통해 연산자에 맞는 계산을 준 풀이.
    for i in range(1, n):
        r = {'+': r + a[i], '-': r - a[i], '*': r * a[i], '/': int(r / a[i])}[s[i-1]]
    ans.append(r)

    # Answer2. 전에 배웠던 eval 함수를 활용한 풀이. (1번에 비해 시간 3배정도 소요)
    for i in range(1, n):
        line += (s[i - 1] + str(a[i]))
        res = int(eval(line))
        line = str(res)
    ans.append(int(line))

print(max(ans), min(ans))