class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        for i in range(x):
            mid = (left+right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                right = mid - 1
            else:
                left = mid + 1
        return mid