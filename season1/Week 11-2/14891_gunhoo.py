import sys
from collections import deque
input = sys.stdin.readline
t = [deque(list(map(int, input().rstrip()))) for _ in range(4)]

k = int(input())
for _ in range(k):
    r = []