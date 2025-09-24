class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [nums[0]] * n
        dp[0] = nums[0]
        dp[1] = nums[1]
        for i in range(2, n):
            dp[i] = nums[i] + dp[i-2]
        return max(dp[-1], dp[-2])