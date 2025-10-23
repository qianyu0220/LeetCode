class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        n = len(s)
        output = 0
        window = set()
        for right,char in enumerate(s):
            while char in window:
                window.remove(s[left]) 
                left += 1
            window.add(s[right])
            output = max(output, right - left + 1)
        return output