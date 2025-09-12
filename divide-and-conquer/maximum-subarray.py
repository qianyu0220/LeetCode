class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        output = nums[0]
        n = len(nums)
        cur_sum = nums[0]
        for i in range(1, n):
            if cur_sum + nums[i] < nums[i]:
                cur_sum = 0
            cur_sum += nums[i]
            output = max(output, cur_sum)
        return output
