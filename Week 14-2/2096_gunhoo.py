# # 일단 세 숫자를 받고, 촤소 경우와 최대 경우 루트를 따로 생성하여 담아버린다.
#
# n = int(input())
#
# a2, b2, c2, a3, b3, c3 = 0, 0, 0, 0, 0, 0
#
# for _ in range(n):
#     a1, b1, c1 = map(int, input().split())
#     a2, b2, c2 = min(a2, b2) + a1, min(a2, b2, c2) + b1, min(b2, c2) + c1
#     a3, b3, c3 = max(a3, b3) + a1, max(a3, b3, c3) + b1, max(b3, c3) + c1
#
# print(max(a3, b3, c3), min(a2, b2, c2))

n = int(input())
graph = []
graph2 = []

for _ in range(n):
    # line = list(map(int, input().split()))
    # graph.append(line)
    # graph2.append(line)
    graph.append()
    print(graph)
    print(graph2)

for i in range(1, n):
    for j in range(3):
        if j == 0:
            graph[i][j] += max(graph[i - 1][j], graph[i - 1][j + 1])
            graph2[i][j] += min(graph2[i - 1][j], graph2[i - 1][j + 1])
        elif j == 1:
            graph[i][j] += max(graph[i - 1][j], graph[i - 1][j + 1], graph[i - 1][j - 1])
            graph2[i][j] += min(graph2[i - 1][j], graph2[i - 1][j + 1], graph2[i - 1][j - 1])
        elif j == 2:
            graph[i][j] += max(graph[i - 1][j], graph[i - 1][j - 1])
            graph2[i][j] += min(graph2[i - 1][j], graph2[i - 1][j - 1])
print(graph)
print(graph2)
print(max(graph[-1]), min(graph2[-1]))