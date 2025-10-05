class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        output = ""
        output += s[0]
        for i in range(1, n-1):
            if s[i] == s[i-1] == s[i+1]:
                return ""
            if s[i] == s[i-1] and s[i] != s[i+1]:
                output += s[i+1]
                output += s[i]
        return output