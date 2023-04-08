import heapq

N, M, K, X = map(int, input().split())
go = [[] for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    go[a].append(b)


def dikstra(go, x, N):
    INF = int(1e9)
    shortest = [INF] * (N + 1)
    heap = []
    heapq.heappush(heap, (0, x))
    while heap:
        distance, node = heapq.heappop(heap)
        if distance > shortest[node]:
            continue
        shortest[node] = distance
        new_distance = distance + 1
        for i in go[node]:
            # 만약 길이 있으면 여기다가 new_distance를 사용한다.
            if new_distance < shortest[i]:
                shortest[i] = new_distance
                heapq.heappush(heap, (new_distance, i))

    return shortest


lst = dikstra(go, X, N)

for i in range(1, len(lst)):
    if lst[i] == K:
        print(i)
if K not in lst[1:]:
    print(-1)