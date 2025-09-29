class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        if x == 0:
            return 0
        for i in range(x):
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1
        return mid