class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}  # Stores the most recent index of each character
        max_length = 0
        start = 0

        for end in range(len(s)):
            if s[end] in char_map:
                start = max(start, char_map[s[end]] + 1)

            char_map[s[end]] = end
            max_length = max(max_length, end - start + 1)

        return max_length