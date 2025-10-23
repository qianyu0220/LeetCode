class Solution:
    def countSubstrings(self, s: str) -> int:
        output = 0
        def count_palindrome(s, left, right):
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                count += 1
            return count
        for i in range(len(s)):
            output += count_palindrome(s, i, i)
            output += count_palindrome(s, i, i+1)
        return output