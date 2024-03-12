class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m, n = len(num1), len(num2)
        result = [0] * (m + n)
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                product = int(num1[i]) * int(num2[j])
                sum_val = result[i + j + 1] + product
                
                result[i + j + 1] = sum_val % 10
                result[i + j] += sum_val // 10
        
        product_str = ''
        leading_zero = True
        
        for digit in result:
            if digit == 0 and leading_zero:
                continue
            leading_zero = False
            product_str += str(digit)
        
        return '0' if not product_str else product_str