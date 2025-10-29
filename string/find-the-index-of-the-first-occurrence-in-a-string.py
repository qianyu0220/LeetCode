class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h = len(haystack)
        n = len(needle)
        if haystack == needle:
            return 0
        for i in range(h+1):
            for j in range(i+1, h+1):
                if haystack[i:j] == needle:
                    return i
        return -1