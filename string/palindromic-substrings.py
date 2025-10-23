class Solution:
    def countSubstrings(self, s: str) -> int:
        output = 0
        def count_palin(s, l, r):
            count = 0
            while l>=0 and r<len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                count += 1
            return count
        for i in range(len(s)):
            output += count_palin(s, i, i)
            output += count_palin(s, i, i+1)
        return output