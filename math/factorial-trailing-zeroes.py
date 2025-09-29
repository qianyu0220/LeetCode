class Solution:
    def trailingZeroes(self, n: int) -> int:
        fives = 0
        i = 5
        while n >= 5:
            n //= 5
            fives += n
        return fives