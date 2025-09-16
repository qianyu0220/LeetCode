class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h = len(haystack)
        n = len(needle)
        if n > h:
            return -1
        for i in range(h):
            if haystack[i: i+n] == needle:
                return i
        return -1