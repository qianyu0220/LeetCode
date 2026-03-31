class Solution:
    def maxArea(self, height: List[int]) -> int:
        output = 0
        n = len(height)
        left, right = 0, n-1
        while left < right:
            if height[left] < height[right]:
                water = height[left] * (right-left)
                left += 1              
            else:
                water = height[right] * (right-left)
                right -= 1               
            output = max(output, water)
        return output 