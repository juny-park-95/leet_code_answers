class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Function to check if there's any repetition in a list
        def has_repetition(nums):
            seen = set()
            for num in nums:
                if num != '.':
                    if num in seen:
                        return True
                    seen.add(num)
            return False

        # Check rows
        for row in board:
            if has_repetition(row):
                return False

        # Check columns
        for col in range(9):
            if has_repetition([board[row][col] for row in range(9)]):
                return False

        # Check 3x3 sub-boxes
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if has_repetition([board[i + x][j + y] for x in range(3) for y in range(3)]):
                    return False

        return True