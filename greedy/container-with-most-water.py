class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        left = 0
        n = len(height)
        right = n - 1
        output = 0
        while left < right:
            if height[left] < height[right]:
                water = height[left] * (right - left)
                left += 1
            else:
                water = height[right] * (right - left)
                right -= 1
            output = max(output, water)
        return output