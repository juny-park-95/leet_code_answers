class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def is_valid_move(board, row, col, num):
            """Check if it's a valid move to place 'num' at position (row, col)."""
            # Check the row and column
            for i in range(9):
                if board[row][i] == num or board[i][col] == num:
                    return False

            # Check the 3x3 box
            start_row, start_col = 3 * (row // 3), 3 * (col // 3)
            for i in range(3):
                for j in range(3):
                    if board[start_row + i][start_col + j] == num:
                        return False

            return True

        def backtrack(board):
            """Try to solve the board using backtracking."""
            for row in range(9):
                for col in range(9):
                    if board[row][col] == ".":
                        for num in map(str, range(1, 10)):  # Try numbers from 1 to 9
                            if is_valid_move(board, row, col, num):
                                board[row][col] = num
                                if backtrack(board):  # Recursively try to solve the rest of the board
                                    return True
                                board[row][col] = "."  # If no solution is found, backtrack
                        return False  # Trigger backtracking if no number can be placed at this position
            return True  # Board is solved

        backtrack(board)
        return board
        