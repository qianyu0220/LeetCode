class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        def expand(l, r):
            while l>=0 and r<n and s[l] == s[r]:
                l -= 1
                r += 1
            return l+1, r
        output = 0
        start, end = 0, 1
        for i in range(n):
            l1, r1 = expand(i,i)
            l2, r2 = expand(i, i+1)
            if end - start < r1 - l1:
                output += 1
            if end - start < r2 - l2:
                output += 1
        return output + n