import time

class NQueens:
    def __init__(self, n):
        self.n = n
        self.board = [-1] * n  # -1 means no queen placed

    def is_safe(self, row, col):
        for i in range(row):
            if self.board[i] == col or abs(self.board[i] - col) == abs(i - row):
                return False
        return True

    def print_board(self):
        for row in range(self.n):
            line = ""
            for col in range(self.n):
                if self.board[row] == col:
                    line += "Q "
                else:
                    line += ". "
            print(line)
        print("\n")
        time.sleep(0.5)  # Pause to visualize step-by-step placement

    def solve_stepwise(self, row=0):
        if row == self.n:
            print("Final Solution:")
            self.print_board()
            return True

        for col in range(self.n):
            if self.is_safe(row, col):
                self.board[row] = col
                print(f"Placing queen at row {row}, col {col}")
                self.print_board()

                if self.solve_stepwise(row + 1):  # Recursive call
                    return True  # Stop at first valid solution
                
                print(f"Backtracking from row {row}, col {col}")
                self.board[row] = -1  # Undo placement

        return False

# Solve and visualize stepwise
solver = NQueens(8)
solver.solve_stepwise()
