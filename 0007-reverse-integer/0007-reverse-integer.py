class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            reversed_str = str(x)[::-1]
            reversed_num = int(reversed_str)
        else:
            reversed_str = str(x)[1:][::-1]
            reversed_num = -int(reversed_str)

        if reversed_num < -2**31 or reversed_num > 2**31 - 1:
            return 0

        return reversed_num
