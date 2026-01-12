class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        output = 0
        n = len(s)
        left = 0
        for right in range(n):
            while s[right] in window:
                window.remove(s[left])
                left += 1
            window.add(s[right])
            output = max(output, right-left+1)
        return output