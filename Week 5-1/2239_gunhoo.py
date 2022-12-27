sudoku = [list(map(int,list(input().rstrip()))) for _ in range(9)]

for i in range(9):
    for j in range(9):
        if not sudoku[i][j]:
            sudoku[i][j] == (i, j)

