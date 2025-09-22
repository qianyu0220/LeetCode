class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        n = len(nums)
        max_sum = nums[0]
        min_sum = nums[0]
        max_cur = nums[0]
        min_cur = nums[0]
        for i in range(1, n):
            max_cur = max(nums[i], max_cur + nums[i])
            min_cur = min(nums[i], min_cur + nums[i])
            max_sum = max(max_sum, max_cur)
            min_sum = min(min_sum, min_cur)
        if max_sum < 0:
            return max_sum
        return max(max_sum, total_sum - min_sum)