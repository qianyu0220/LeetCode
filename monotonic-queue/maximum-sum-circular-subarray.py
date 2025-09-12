class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        min_cur = max_cur = min_sum = max_sum = nums[0]
        for i in range(1, len(nums)):
            max_cur = max(nums[i], max_cur + nums[i])
            max_sum = max(max_cur, max_sum)
            min_cur = min(nums[i], min_cur + nums[i])
            min_sum = min(min_cur, min_sum)
        if max_sum < 0:
            return max_sum
        return max(max_sum, total_sum - min_sum)