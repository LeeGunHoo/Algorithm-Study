import sys

n1, n2 = map(int, sys.stdin.readline().split())
g1 = list(map(str,sys.stdin.readline().rstrip("\n")))
g2 = list(map(str,sys.stdin.readline().rstrip("\n")))
t = int(sys.stdin.readline())

g1.reverse()
l = g1 + g2

ans = ''

for _ in range(t):
    for i in range(len(l) - 1):
        if l[i] in g1 and l[i+1] in g2:
            l[i], l[i+1] = l[i+1], l[i]
            if l[i+1] == g1[-1]:
                break
for i in l:
    ans += i

print(ans)