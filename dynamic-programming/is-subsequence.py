class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p = 0
        q = 0
        m = len(s)
        n = len(t)
        output = 0
        for i in range(n):
            if p < m and s[p] == t[q]:
                output += 1
                p += 1
            q += 1
        return len(s) == p
            
