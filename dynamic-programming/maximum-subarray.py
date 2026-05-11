class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        output = 0
        cur_sum = 0
        for i in range(n):
            if cur_sum + nums[i] < nums[i]:
                cur_sum = 0
            cur_sum += nums[i]
            output = max(output, cur_sum)
        return output