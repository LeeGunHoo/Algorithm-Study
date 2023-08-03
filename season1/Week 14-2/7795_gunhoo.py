# t = int(input())
#
# for _ in range(t):
#     n, m = map(int, input().split())
#     A = sorted(list(map(int, input().split())))
#     B = sorted(list(map(int, input().split())))
#     ans = 0
#     i = 0
#     for a in A:
#         while i < m and a > B[i]:
#             i += 1
#         ans += i
#
#     print(ans)

def binary_search(l, x):
    start = 0
    end = len(l) - 1
    while start <= end:
        mid = (start + end) // 2
        if l[mid] < x:
            start = mid + 1
        else:
            end = mid - 1
    return start

t = int(input())
while t:
    t -= 1
    cnt = 0
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b.sort()
    for i in a:
        cnt += binary_search(b, i)
print(cnt)