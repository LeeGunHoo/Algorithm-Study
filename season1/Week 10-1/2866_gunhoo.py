R, C = map(int, input().split())
string_lst = []
for _ in range(R):
    string_lst.append(input())
print(string_lst)
l2 = ["" for _ in range(C)]

for i in range(R - 1, -1, -1):
    s = set([])
    for j in range(C):
        l2[j] += string_lst[i][j]
        print(l2)
        s.add(l2[j])
        print(s)
    if len(s) == C:
        ans = i
        break

print(ans)