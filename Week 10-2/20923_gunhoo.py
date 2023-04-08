import sys

n, m = map(int, input().split())
deck, ground = [[], []], [[], []]
# 누가 카드 뒤집을 차례인지 알려주는 변수
# 0:do 1:su
player = 0
for _ in range(n):
  do, su = map(int, input().split())
  deck[0].append(do)
  deck[1].append(su)

for _ in range(m):
  bell = -1
  ground[player].append(deck[player].pop())
    # 플레이어의 덱이 사라지면 바로 종료
  if len(deck[player]) == 0:
    break
    # 그라운드 위의 숫자가 5이면 do가 종 침
  if ground[player][-1] == 5:
    bell = 0
    # 그라운드 숫자의 합이 5이면 su가 종 침
  elif ground[0] and ground[1] and ground[player][-1] + ground[1-player][-1] == 5:
    bell = 1
    # 그라운드의 모든 카드를 (상대꺼 먼저) 종 친 사람 덱 맨 아래에 넣어줌
  if bell == 0 or bell == 1:
    for i in [1 - bell, bell]:
      while ground[i]:
        deck[bell] = [ground[i].pop(0)] + deck[bell]
  player = 1 - player

if len(deck[0]) > len(deck[1]):
  print('do')
elif len(deck[0]) < len(deck[1]):
  print('su')
else:
  print('dosu')
