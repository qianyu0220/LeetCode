class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        output = 0
        while left < right:
            if height[left] < height[right]:
                water = (right - left) * height[left]
                left += 1
            else:
                water = (right - left) * height[right]
                right -= 1
            output = max(output, water)
        return output