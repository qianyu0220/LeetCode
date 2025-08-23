class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        output = 1
        char_set = set()
        left = 0
        for right in range(n):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            output = max(output, right - left + 1)
        return output
