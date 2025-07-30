class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_water = 0

        while left < right:
            if height[left] < height[right]:
                left += 1
                max_water = max(max_water, (min(height[left], height[right]) * (right - left)))
            elif height[left] > height[right]: 
                right -= 1
                max_water = max(max_water, (min(height[left], height[right]) * (right - left)))
            else:
                max_water = max(max_water, (height[left]) * (right - left))
            return max_water
