class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n = -n
            x = 1/x
        result = 1
        while n > 0:
            if n % 2 == 1:
                result *= x
            n = n // 2
            x = x ** 2
        return result
