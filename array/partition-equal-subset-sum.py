class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        n = len(nums)
        dp = [False] * (target + 1)
        dp[0] = True
        for i in range(1, target+1):
            for num in nums:
                if dp[i-num]:
                    dp[i] = True
        return dp[-1]