class Solution:
    def isPalindrome(self, s: str) -> bool:
        tmp = ""
        for char in s.lower():
            if char.isdigit() or char.isalpha():
                tmp += char
        return tmp == tmp[::-1]