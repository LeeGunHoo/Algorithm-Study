n, l = map(int, input().split())
water = list(map(int, input().split()))

water.sort()
point = water[0]
cnt = 1

for i in range(1, n):
    if water[i] in range(point, point + l):
        continue
    else:
        point = water[i]
        cnt += 1

print(cnt)

