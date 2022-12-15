# dfs로 풀어보자. 문제는 각 노드끼리 어떻게 연결하느냐...
# 그래프 자료구조 때를 생각해보면 결국 배열 아니면 링크드 리스트
# 링크드 리스트는 코테에서는 엔간하면 자제해보자. 테스트 케이스 많아지면 언제 터질지 모르니!!

n = int(input())
e = int(input())
computer = [[0]*(n+1) for _ in range(n+1)]

def dfs(n):
    checked =  []
    stack = [n]
    while stack:
        s = stack.pop()
        if s not in checked:
            checked.append(s)
            for k in range(len(computer[s])):
                if computer[s][k] == 1:
                    stack.append(k)
    print(checked)
    return checked

for _ in range(e):
    i, j = map(int, input().split())
    computer[i][j] += 1
    computer[j][i] += 1

l = dfs(1)
print(len(l) - 1)

# 예제는 맞게 나오는데 틀림.,...
