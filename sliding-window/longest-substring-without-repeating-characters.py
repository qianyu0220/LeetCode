class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        output = 0
        left = 0
        n = len(s)
        for right in range(n):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            output = max(output, right - left + 1)
        return output