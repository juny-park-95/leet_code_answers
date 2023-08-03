class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate_parentheses(combination, open_count, close_count):
            if open_count == n and close_count == n:
                result.append(combination)
                return

            if open_count < n:
                generate_parentheses(combination + '(', open_count + 1, close_count)

            if close_count < open_count:
                generate_parentheses(combination + ')', open_count, close_count + 1)

        result = []
        generate_parentheses('', 0, 0)
        return result