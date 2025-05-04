def is_safe(board, row, col, n):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == row - i:
            return False
    return True

def print_board(board):
    n = len(board)
    for row in range(n):
        line = ""
        for col in range(n):
            line += "Q " if board[row] == col else ". "
        print(line)
    print("\nColumn positions:", board)

def solve_n_queens(row, board, n):
    if row == n:
        print("\n✅ Solution Found:")
        print_board(board)
        return True
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            if solve_n_queens(row + 1, board, n):
                return True
    return False

def n_queens(n):
    board = [-1] * n
    if not solve_n_queens(0, board, n):
        print("No solution")


n_queens(8)
