class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        len_s = len(s)
        len_t = len(t)
        i = j = 0
        output = ""
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                output += s[i]
                i += 1
            j += 1
        return output == s