class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]  # Initialize stack with -1 to act as base
        max_length = 0

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()  # Pop the matching '('
                if not stack:
                    stack.append(i)  # Push current index as new base
                else:
                    max_length = max(max_length, i - stack[-1])

        return max_length