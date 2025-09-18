class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        output = -float("inf")
        if n == 1:
            return nums[0]
        for i in range(1, n):
            output = max(output, nums[i] * nums[i-1])
        return output