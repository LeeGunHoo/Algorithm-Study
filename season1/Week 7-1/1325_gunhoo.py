from collections import deque
import sys

com,hint=map(int,input().split())

#신뢰관계
trust=[[] for _ in range(com+1)]
for _ in range(hint):
  a,b=map(int, sys.stdin.readline().rstrip().split())
  trust[b].append(a)

#도달가능한 컴퓨터 수
answer=[0 for _ in range(com+1)]

#bfs
for i in range(1,com+1):
  count=0
  cap=[False for _ in range(com+1)]
  queue=deque([i])
  while queue:
    tmp=queue.popleft()
    count+=1
    for j in trust[tmp]:
      if not cap[j]:
        queue.append(j)
        cap[tmp] = True

  answer[i]=count
maxi=max(answer)

for i in range(1,com+1):
  if answer[i]==maxi:
    print(i,end=' ')