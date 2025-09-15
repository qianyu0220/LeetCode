class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        reversed_words = words[::-1]
        output = " ".join(reversed_words)
        return output