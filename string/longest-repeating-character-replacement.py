class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        n = len(s)
        output = 0
        cur_freq = 0
        left = 0
        for right in range(n):
            count[s[right]] = count.get(s[right], 0) + 1
            while right - left + 1 - count[s[right]] > k:
                count[s[left]] -= 1
                left += 1
            output = max(output, right - left + 1)
        return output