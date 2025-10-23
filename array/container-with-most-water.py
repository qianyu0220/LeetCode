class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        n = len(height)
        left = 0
        right = n - 1
        while left < right:
            if height[left] < height[right]:
                water = (right - left) * height[left]
                left += 1
            else:
                water = (right - left) * height[right]
                right -= 1
            max_water = max(max_water, water)
        return max_water