class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:  # If the array is empty, return an empty string
            return ""

        prefix = strs[0]  # Initialize the prefix with the first string

        for string in strs[1:]:
            while string[:len(prefix)] != prefix:
                prefix = prefix[:-1]  # Remove the last character from the prefix

                if not prefix:  # If the prefix becomes empty, there's no common prefix
                    return ""

        return prefix
