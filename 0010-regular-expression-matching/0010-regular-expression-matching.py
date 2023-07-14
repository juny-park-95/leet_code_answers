class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        for i in range(m):
            for j in range(n):
                if p[j] == '.' or p[j] == s[i]:
                    dp[i + 1][j + 1] = dp[i][j]
                elif p[j] == '*':
                    if p[j - 1] == '.' or p[j - 1] == s[i]:
                        dp[i + 1][j + 1] = dp[i][j + 1] or dp[i + 1][j - 1]
                    else:
                        dp[i + 1][j + 1] = dp[i + 1][j - 1]

        return dp[m][n]
