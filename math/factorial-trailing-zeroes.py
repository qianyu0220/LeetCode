class Solution:
    def trailingZeroes(self, n: int) -> int:
        fives = 0
        i = 5
        while i <= n:
            n = n // 5
            fives += n
        return fives