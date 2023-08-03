# 문제 이해를 잘 못하겠음.
# 그냥 오른쪽에 반경 큰 순서대로 쌓는다고 생각하기로 함.
# 스택 구조 유력.
# 결국 가장 큰게 나올때까지는 2번에 다 덜어내야함.

n = int(input())
l1 = list(map(int, input().split()))
l2 = []
l3 = []
ans = []

for i in range(n, 0, -1):
    # 역순으로 반복문을 돌려서, 해당되는 가장 큰 원판이 1번에 남아있다면
    if i in l1:
        while 1:
            # 가장 큰 원판이 등장했다면 3번으로 ㄱㄱ
            if l1[-1] == i:
                l3.append(l1.pop())
                ans.append('1 3')
                break
            # 가장 큰게 아니라면 2번으로 ㄱㄱ
            l2.append(l1.pop())
            ans.append('1 2')
    # 1번에 남아있지 않다면 2번일거다.
    else:
        while 1:
            if l2[-1] == i:
                l3.append(l2.pop())
                ans.append('2 3')
                break
            l1.append(l2.pop())
            ans.append('2 1')

print(len(ans))
for i in ans:
    print(i)
