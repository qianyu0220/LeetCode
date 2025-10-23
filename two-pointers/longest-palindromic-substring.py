class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        output = ""
        def count(l,r):
            while l>=0 and r<len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return l+1, r
        start, end = 0, 1
        for i in range(len(s)):
            l1, r1 = count(i, i)
            l2, r2 = count(i, i+1)
            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2
        return s[start: end]