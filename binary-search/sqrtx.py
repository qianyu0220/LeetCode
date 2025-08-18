class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        left, right = 1, x
        while left < right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left += 1
            elif mid * mid > x:
                right -= 1
        return mid