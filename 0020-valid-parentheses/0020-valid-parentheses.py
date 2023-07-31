class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}

        for ch in s:
            if ch in '({[':
                stack.append(ch)
            elif ch in ')}]':
                if not stack or stack[-1] != bracket_map[ch]:
                    return False
                stack.pop()

        return not stack