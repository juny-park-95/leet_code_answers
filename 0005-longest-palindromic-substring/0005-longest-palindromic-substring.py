class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) < 2:
            return s

        start, end = 0, 0

        def expandAroundCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1

        if len(s) == 1:
            return s

        for i in range(len(s) - 1):
            len1 = expandAroundCenter(i, i)
            len2 = expandAroundCenter(i, i + 1)
            maxLen = max(len1, len2)
            if maxLen > end - start:
                start = i - (maxLen - 1) // 2
                end = i + maxLen // 2

        return s[start:end+1]