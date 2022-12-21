# 이건 많이 풀어봤던 문제
n = int(input())
num = [1]*10

for _ in range(n-1):
    for i in range(1, 10):
        num[i] += num[i-1]

print(sum(num)%10007)