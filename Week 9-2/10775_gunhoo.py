import sys

gate_num = int(input())
gate = [i for i in range(0, gate_num + 1)]
num = int(input())

answer = 0
for _ in range(num):
    plane = int(input())
    # 들어갈 자리가 있을 경우
    if gate[plane] == plane:
        gate[plane] -= 1
        answer += 1
    else:
        now = plane

        while True:
            if gate[now] == now:
                # 들어갈 자리가 타고가다보면 나올 경우
                gate[now] -= 1
                gate[plane] = now
                answer += 1
                break
            if gate[now] == 0:
                # 들어갈 자리가 타고가도 안나오는 경우
                print(answer)
                sys.exit(0)
            now = gate[now]

print(answer)