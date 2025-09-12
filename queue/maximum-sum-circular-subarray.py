class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        cur_min = cur_max = max_sum = min_sum = nums[0]
        n = len(nums)
        for i in range(1, n):
            cur_max = max(cur_max + nums[i], nums[i])
            max_sum = max(max_sum, cur_max)

            cur_min = min(nums[i], cur_min + nums[i])
            min_sum = min(cur_min, min_sum)
        if max_sum < 0:
            return max_sum
        return max(max_sum, total_sum - min_sum)