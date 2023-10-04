class Solution:
    def countAndSay(self, n):  # Using forward declaration for the return type
        if n == 1:
            return "1"

        prev_str = self.countAndSay(n-1)
        result = []
        count = 1

        # Iterate over the string returned from the previous call
        for i in range(1, len(prev_str)):
            # If the current character is the same as the previous one, increase the count
            if prev_str[i] == prev_str[i-1]:
                count += 1
            else:
                # Otherwise, append the count and the previous character to the result
                result.append(str(count))
                result.append(prev_str[i-1])
                count = 1

        # Handle the last set of characters
        result.append(str(count))
        result.append(prev_str[-1])

        return ''.join(result)