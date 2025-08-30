class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        output = 0
        n = len(nums)
        cur_sum = 0
        for i in range(n):
            if nums[i] + cur_sum < nums[i]:
                cur_sum = 0
            cur_sum += nums[i]
            output = max(cur_sum, output)
        return output