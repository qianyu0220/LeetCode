class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        dp = [False] * (target+1)
        dp[0] = True

        for num in nums:
            for j in range(1, target+1):
                if dp[j-num]:
                    dp[j] = True
        return dp[target]