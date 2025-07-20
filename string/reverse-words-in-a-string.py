class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        reversed_words = words[::-1]
        reversed_strings = ' '.join(reversed_words)
        return reversed_strings