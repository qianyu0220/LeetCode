class Solution:
    def longestPalindrome(self, s: str) -> str:
        def build(i, j):
            while i>=0 and j<len(s) and s[i]==s[j]:
                i -= 1
                j += 1
            return s[i+1:j]
        result = ""
        for i in range(len(s)):
            odd = build(i, i)
            even = build(i, i+1)
            if len(odd) > len(result):
                result = odd
            if len(even) > len(result):
                result = even
        return result