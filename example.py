import itertools

n = list(input().split())

square = []
notSquare = []

com = list(itertools.combinations(n, 2))

def issquare(n):
	temp = n ** 0.5
	if int(temp) == temp:
		return True
	else:
		return False

def bfs(n):
