class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        n = len(s)
        output = 0
        length = 0
        for left in range(n):
            for right in range(left+1, n):
                while s[right] in set(s[left:right]):
                    left += 1
                    length = right - left + 1
                output = max(output, length)
        return output