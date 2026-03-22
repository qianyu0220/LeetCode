class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        n = len(nums)
        
        for left in range(0, n - k + 1):
            window = []
            for right in range(left, left + k):
                window.append(nums[right])
            output.append(max(window))
        return output


