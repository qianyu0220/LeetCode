class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_haystack = len(haystack)
        len_needle = len(needle)
        output = 0
        if len_needle > len_haystack:
            return -1
        for i in range(len_needle):
            if haystack[i:i+len_needle] == needle:
                return i
        return -1