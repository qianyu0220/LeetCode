class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        rain_water = 0
        for i in range(n):
            left_max = max(height[:i+1])
            right_max = max(height[i:])
            rain_water += min(left_max, right_max) - height[i]
        return rain_water