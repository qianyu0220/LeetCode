class Solution:
    def maxArea(self, height: List[int]) -> int:
        cur_max = 0
        n = len(height)
        left = 0
        right = n - 1
        while left < right:
            if height[left] < height[right]:
                water =  height[left] * (right - left)
                left += 1
            else:
                water = height[right] * (right - left)
                right -= 1
            cur_max = max(water, cur_max)
        return cur_max