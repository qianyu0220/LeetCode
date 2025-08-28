class Solution:
    def isPalindrome(self, s: str) -> bool:
        output = ""
        for char in s.lower():
            if char.isdigit() or char.isalpha():
                output += char
        return True if output == output[::-1] else False
