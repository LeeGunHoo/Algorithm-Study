n = int(input())
l = [0]

for i in range(1, n+1):
    l.append(1 + min(l[i - (j+1) ** 2] for j in range(int(i ** 0.5))))

print(l[-1])