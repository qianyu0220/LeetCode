class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        cur_sum = nums[0]
        output = nums[0]
        for right in range(1, n):
            if cur_sum + nums[right] < nums[right]:
                cur_sum = 0
            cur_sum += nums[right]
            output = max(output, cur_sum)
        return output
