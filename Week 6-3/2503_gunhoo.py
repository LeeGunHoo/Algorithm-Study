from itertools import permutations

l = [''.join(map(str, i)) for i in permutations(range(1, 10), 3)]

for _ in range(int(input())):
    r, s, b = map(int,  input().split())
    r = str(r)
    for n in l[::-1]:
        strike = 0
        ball = 0
        for i in range(3):
            if n[i] == r[i]:
                strike += 1
            elif n[i] in r:
                ball += 1
        if (strike, ball) != (s, b):
            l.remove(n)

print(len(l))