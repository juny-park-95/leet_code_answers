class Solution:
    def myAtoi(self, s: str) -> int:
        # Remove leading whitespace
        s = s.lstrip()

        if len(s) == 0:
            return 0

        # Check if the number is negative or positive
        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        # Read digits until the next non-digit character
        digits = []
        for char in s:
            if not char.isdigit():
                break
            digits.append(char)

        if len(digits) == 0:
            return 0

        # Convert digits to integer
        num = int(''.join(digits))

        # Apply sign
        num *= sign

        # Clamp to 32-bit signed integer range
        num = max(min(num, 2**31 - 1), -2**31)

        return num
