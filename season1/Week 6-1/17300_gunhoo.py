input()

l = list(map(int, input().split()))
dictionary = {(1, 3): 2, (1, 7): 4, (1, 9): 5, (2, 8): 5, (3, 7): 5, (3, 9): 6, (4, 6): 5, (7, 9): 8}

if len(l) != len(set(l)):
    print("NO")
    quit()

for i, p in enumerate(zip(l, l[1:])):
    p = tuple(sorted(p))
    if p in dictionary:
        print(i)
        print(l[:i])
        if dictionary[p] not in l[:i]:
            print("NO")
            break
else:
    print("YES")