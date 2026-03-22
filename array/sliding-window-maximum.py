class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        n = len(nums)

        if n == 1:
            return nums
        
        for left in range(0, n - 2):
            window = []
            for right in range(left, left + 3):
                window.append(nums[right])
            output.append(max(window))
        return output


