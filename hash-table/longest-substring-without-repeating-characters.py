class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 
        n = len(s)
        window = set()
        output = 0
        for right, char in enumerate(s):
            while char in window:
                window.remove(s[left])
                left += 1
            window.add(char)
            output = max(output, right-left+1)
        return output
        
