class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h = len(haystack)
        n = len(needle)
        if haystack == needle:
            return 0
        for i in range(h):
            for j in range(i+1, h):
                if haystack[i:j] == needle:
                    return i
        return -1