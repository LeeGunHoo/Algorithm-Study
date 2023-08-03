import sys

t = int(input())

for _ in range(t):
    l = []
    n = int(input())
    for i in range(n):
        s = list(sys.stdin.readline().rstrip("\n"))
        l.append([i, s])
    for i in range(len(l[0][1])):
        tmp = [t[1][i] for t in l]
        if len(set(tmp)) == 2:
            if 'R' not in set(tmp):
                l = [t for t in l if t[1][i] == 'S']
            elif 'S' not in set(tmp):
                l = [t for t in l if t[1][i] == 'P']
            elif 'P' not in set(tmp):
                l = [t for t in l if t[1][i] == 'R']
        if not l:
            break
    if len(l) > 1:
        print(0)
    else:
        print(l[0][0] + 1)