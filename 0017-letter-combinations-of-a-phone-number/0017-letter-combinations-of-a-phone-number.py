class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def generate_combinations(digits, current_combination, index, result):
            if index == len(digits):
                result.append(current_combination)
                return

            current_digit = digits[index]
            letters = digit_to_letters[current_digit]

            for letter in letters:
                generate_combinations(digits, current_combination + letter, index + 1, result)

        result = []
        if digits:
            generate_combinations(digits, "", 0, result)
        return result