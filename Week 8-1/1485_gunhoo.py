# 정사각형이 만들어지려면 결국 두 점을 이은 길이가 세 쌍이면 되지 않을까??

T = int(input())

for _ in range(T):
    square = []

    for _ in range(4):
        square.append(tuple(map(int, input().split())))

    if len(set([((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) for a in square for b in square])) == 3:
        print(1)
    else:
        print(0)