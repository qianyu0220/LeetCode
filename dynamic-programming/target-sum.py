class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        S = sum(nums)
        n = len(nums)
        sum_P = (target +S) // 2
        if  (S+target) %2 != 0 or S < target:
            return 0
        dp = [0] * (n+1)
        dp[0] = 0
        for i in range(1, n+1):
            for num in nums:
                dp[i] += dp[i-num]