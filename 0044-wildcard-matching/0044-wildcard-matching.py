class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Initialize a 2D DP table
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]

        # Base case: an empty pattern matches an empty string
        dp[0][0] = True

        # Fill the first row of the DP table
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]

        # Fill the DP table
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == s[i - 1] or p[j - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]

        # The result is in the bottom-right cell of the DP table
        return dp[len(s)][len(p)]