class Solution:
    def checkValidString(self, s: str) -> bool:
        l = 0
        r = 0
        star = 0
        for c in s:
            if c == "(":
                l += 1
            elif c == ")":
                r += 1
            elif c == "*":
                star += 1
        if l == r:
            return True
        elif l+star == r or l == r+star:
            return True
        return False

