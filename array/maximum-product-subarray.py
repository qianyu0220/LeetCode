class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        output = -float("inf")
        for i in range(1, n):
            if nums[i] == 0:
                continue
            output = max(output, nums[i] * nums[i-1])
        return output