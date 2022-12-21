# 메모제이션을 사용하기 위해 귀납적 접근을 해보자
# f(n)이 완성되려면 f(n-2)에서 한 경우 (세로 추가), f(n-2)에서 한 경우(가로가로 추가)가 있다.
# f(n) = f(n-1) + f(n-2)
# 피보나치를 예로 생각해보면, 결국 임의의 k에 대한 f(k)를 저장해놓으면 된다.

# 근데 길이 1000짜리 배열을 만들자니 너무 크긴하다...
# 3칸으로 줄일 수 있을 것 같다.

from collections import deque

n = int(input())
dp = deque([0, 1, 2, 3])
if n <= 3:
    print(dp[n])
else:
    for i in range(3, n):
        dp[i] = dp[i - 1] + dp[i - 2]
        dp.popleft()

    print(dp[n] % 10007)