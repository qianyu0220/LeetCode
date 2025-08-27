class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        char_set = set()
        output = 0
        n = len(s)
        for right in range(n):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            output = max(right-left+1, output)
        return output