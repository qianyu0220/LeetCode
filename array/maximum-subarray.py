class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = nums[0]
        max_sum = nums[0]
        n = len(nums)
        for i in range(1, n):
            if cur_sum + nums[i] < nums[i]:
                cur_sum = 0
            cur_sum += nums[i]
            max_sum = max(cur_sum, max_sum)
        return max_sum