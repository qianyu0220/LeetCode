class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        tmp = ""
        i = j = 0
        while i<n and j<m:
            if s[i] == t[j]:
                tmp += s[i]
                i += 1
            j += 1
        return s == tmp