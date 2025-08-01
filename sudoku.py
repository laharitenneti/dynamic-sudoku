import copy

#isValid checks for the presence of num in row/col/subgrid
def isValid(board, row, col, num, r, c):
    n = len(board)
    if num in board[row]:
        return False
    for i in range(n):
        if board[i][col] == num:
            return False
    #floor division for obtaining start, end of subgrid
    subrow = (row // r) * r
    subcol = (col // c) * c
    for i in range(r):
        for j in range(c):
            if board[subrow + i][subcol + j] == num:
                return False
    return True

def check_sud(square, r, c):
    n = len(square)
    #checks for a valid row (i.e., w/o repetitions)
    for row in square:
        cl = list(range(1, n + 1))
        for i in row:
            if i not in cl:
                return False
            cl.remove(i)
    #checks for a valid col
    for col in range(n):
        cl = list(range(1, n + 1))
        for row in square:
            if row[col] not in cl:
                return False
            cl.remove(row[col])
    #checks for valid subgrid
    for row_start in range(0, n, r):
        for col_start in range(0, n, c):
            seen = []
            for i in range(r):
                for j in range(c):
                    val = square[row_start + i][col_start + j]
                    seen.append(val)
            if sorted(seen) != list(range(1, n + 1)):
                return False
    return True

#solution
def correct(sudoku, r, c):
    n = len(sudoku)
    for i in range(n):
        for j in range(n):
            if sudoku[i][j] == 0:
                for num in range(1, n + 1):
                    if isValid(sudoku, i, j, num, r, c):
                        sudoku[i][j] = num
                        if correct(sudoku, r, c):
                            return True
                        sudoku[i][j] = 0
                return False
    return True

#Printing the grid
def printSudoku(sudoku):
    for row in sudoku:
        print(" ".join(str(val) for val in row))

# -----User-----

n = int(input("Enter Sudoku size (e.g., 6, 9, 12): "))
r = int(input("Enter subgrid rows (e.g., 2 for 2×3 subgrid): "))
c = int(input("Enter subgrid columns (e.g., 3 for 2×3 subgrid): "))

if r * c != n:
    print("Invalid dimensions. Subgrid rows × cols must equal board size.")
    exit()

sudoku = []
print("Enter the board row by row:")
for _ in range(n):
    row = [int(val) for val in input().split()]
    sudoku.append(row) #Creating the grid

sudoku_copy = copy.deepcopy(sudoku) #Deepcopy to avoid modifying the original grid.
for i in range(n):
    for j in range(n):
        if sudoku_copy[i][j] == 0:
            num = int(input(f"Enter number to be filled in sudoku [{i},{j}]: "))
            sudoku_copy[i][j] = num #Accepting the user's values

#Checking for accuracy
if check_sud(sudoku_copy, r, c):
    print("\nYour sudoku is valid")
else:
    print("\nHmm. Your answer was incorrect.\nHere's the correct solution:\n")
    correct(sudoku, r, c)
    printSudoku(sudoku)
