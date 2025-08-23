class Solution:
    def mySqrt(self, x: int) -> int:
        left = 1
        right = x
        if x == 0:
            return 0
        while left < right:
            mid = (left+right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                right = mid - 1
            else:
                left = mid + 1
        return mid