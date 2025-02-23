def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def print_board(board):
    n = len(board)
    for row in range(n):
        line = ""
        for col in range(n):
            if board[row] == col:
                line += "Q "
            else:
                line += ". "
        print(line)
    print("\n")

def solve_n_queens(n, row=0, board=[]):
    if row == n:
        print_board(board)  # Print the matrix solution
        return True

    for col in range(n):
        if is_safe(board, row, col):
            board.append(col)
            if solve_n_queens(n, row + 1, board):
                return True  # Stop at first valid solution
            board.pop()  # Backtrack

    return False

# Solve for 8-queens
solve_n_queens(8)
