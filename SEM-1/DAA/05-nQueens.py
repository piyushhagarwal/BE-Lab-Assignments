from typing import List

class Solution:
    
    # Method to check if placing a queen at a given position is possible
    def is_safe(self, n: int, row: int, col: int, board: List[List[str]]) -> bool:
        # Check the row on the left side
        for y in range(col):
            if board[row][y] == 'Q':
                return False

        # Check the upward diagonal on the left side
        x, y = row, col
        while x >= 0 and y >= 0:
            if board[x][y] == 'Q':
                return False
            x -= 1
            y -= 1

        # Check the downward diagonal on the left side
        x, y = row, col
        while x < n and y >= 0:
            if board[x][y] == 'Q':
                return False
            x += 1
            y -= 1

        return True

    # Recursive method to solve the N-Queens problem
    def solve_n_queens_util(self, n: int, col: int, board: List[List[str]], solutions: List[List[str]]):
        # Base case: If all queens are placed, add the current solution to solutions
        if col >= n:
            current_solution = []
            for i in range(n):
                row_str = ""
                for j in range(n):
                    row_str += board[i][j]
                current_solution.append(row_str)
            solutions.append(current_solution)
            return

        # Try placing a queen in each row of the current column
        for row in range(n):
            # Check if it is safe to place the queen at board[row][col]
            if self.is_safe(n, row, col, board):
                # Place the queen
                board[row][col] = 'Q'
                # Recur to place the rest of the queens
                self.solve_n_queens_util(n, col + 1, board, solutions)
                # Backtrack: Remove the queen from board[row][col]
                board[row][col] = '.'

    # Main method to solve the N-Queens problem
    def solveNQueens(self, n: int) -> List[List[str]]:
        solutions = []
        # Create an empty n x n board with all cells initialized to '.'
        board = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append('.')
            board.append(row)

        # Start solving the N-Queens problem
        self.solve_n_queens_util(n, 0, board, solutions)

        return solutions

def test_n_queens():
    solution = Solution()
    
    # Test case 1: n = 1
    print("Test case n = 1:")
    solutions = solution.solveNQueens(1)
    for board in solutions:
        for row in board:
            print(row)
        print()
    print(f"Number of solutions for n = 1: {len(solutions)}\n")
    
    # Test case 2: n = 4
    print("Test case n = 4:")
    solutions = solution.solveNQueens(4)
    for board in solutions:
        for row in board:
            print(row)
        print()
    print(f"Number of solutions for n = 4: {len(solutions)}\n")
    
    # Test case 3: n = 8 (classic 8-queens problem)
    print("Test case n = 8:")
    solutions = solution.solveNQueens(8)
    for board in solutions[:2]:  # Print only the first two solutions to avoid too much output
        for row in board:
            print(row)
        print()
    print(f"Number of solutions for n = 8: {len(solutions)}\n")

# Run the test function
test_n_queens()
