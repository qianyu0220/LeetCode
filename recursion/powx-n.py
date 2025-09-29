class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = 1
        if n < 0:
            n = -n
            x = 1/x
        while n > 0:
            if n % 2 == 1:
                result = result * x
            n = n // 2
            x *= x
        return result