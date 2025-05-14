# Sudoku Solver

def print_board(board):
    for i in range(9):
        row = ""
        for j in range(9):
            row += str(board[i][j]) + " "
            if (j + 1) % 3 == 0 and j != 8:
                row += "| "
        print(row)
        if (i + 1) % 3 == 0 and i != 8:
            print("- - - + - - - + - - -")

def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:  # 0 represents an empty cell
                return (i, j)
    return None

def is_valid(board, num, pos):
    row, col = pos

    # Check row
    for j in range(9):
        if board[row][j] == num and j != col:
            return False

    # Check column
    for i in range(9):
        if board[i][col] == num and i != row:
            return False

    # Check 3x3 grid
    box_row = (row // 3) * 3
    box_col = (col // 3) * 3

    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True

def solve(board):
    empty = find_empty(board)
    if not empty:
        return True  # Puzzle solved

    row, col = empty

    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num

            if solve(board):
                return True

            board[row][col] = 0  # Backtrack

    return False

# Example unsolved board (0 means empty)
sudoku_board = [
    [5, 1, 7, 6, 0, 0, 0, 3, 4],
    [2, 8, 9, 0, 0, 4, 0, 0, 0],
    [3, 4, 6, 2, 0, 5, 0, 9, 0],
    [6, 0, 2, 0, 0, 0, 0, 1, 0],
    [0, 3, 8, 0, 0, 6, 0, 4, 7],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 9, 0, 0, 0, 0, 0, 7, 8],
    [7, 0, 3, 4, 0, 0, 5, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

print("Unsolved Sudoku:")
print_board(sudoku_board)

if solve(sudoku_board):
    print("\nSolved Sudoku:")
    print_board(sudoku_board)
else:
    print("No solution exists.")
