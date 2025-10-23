class Solution:
    def maxArea(self, height: List[int]) -> int:
        # max_water = 0
        # left = 0
        # right = len(height) - 1
        # while left < right:
        #     if height[left] <= height[right]:
        #         water = height[left] * (right - left)
        #         left += 1
        #     else:
        #         water = height[right] * (right - left)
        #         right -= 1
        #     max_water = max(max_water, water)
        # return max_water
        max_water = 0
        left = 0
        right = len(height) - 1
        while left < right:
            if height[left] < height[right]:
                water = (right - left) * height[left]
                left += 1
            else:
                water = (right - left) * height[right]
                right -= 1
            max_water = max(water, max_water)
        return max_water
