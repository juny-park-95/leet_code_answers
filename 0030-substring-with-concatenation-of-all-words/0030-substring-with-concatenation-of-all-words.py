class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_length = len(words[0])
        total_length = word_length * len(words)
        words_count = {}
        result = []

        for word in words:
            words_count[word] = words_count.get(word, 0) + 1

        for i in range(word_length):
            left = i
            right = i
            current_words_count = {}

            while right + word_length <= len(s):
                current_word = s[right:right + word_length]
                right += word_length

                if current_word in words_count:
                    current_words_count[current_word] = current_words_count.get(current_word, 0) + 1

                    while current_words_count[current_word] > words_count[current_word]:
                        current_words_count[s[left:left + word_length]] -= 1
                        left += word_length

                    if right - left == total_length:
                        result.append(left)

                else:
                    current_words_count.clear()
                    left = right

        return result