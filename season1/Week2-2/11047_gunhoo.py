N, K = map(int, input().split())
coin = []
answer = 0
remain = K
for _ in range(N):
    coin.append(int(input()))

coin.reverse()

for i in coin:
    answer += remain // i
    remain = remain % i

print(answer)