class Solution:
    def checkValidString(self, s: str) -> bool:
        low = high = 0
        for i in range(len(s)):
            if s[i] == "(":
                low+=1
                high+=1
            elif s[i] == ")":
                low -= 1
                high -= 1
            elif s[i] == "*":
                low -= 1
                high += 1
            if high < 0:
                return False
            low = max(0, low)
        return low == 0