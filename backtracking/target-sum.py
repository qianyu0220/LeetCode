class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        self.count = 0
        def dfs(i, cur_sum):
            if i == n:
                if cur_sum == target:
                    self.count += 1
                return
            dfs(i+1, cur_sum + nums[i])
            dfs(i+1, cur_sum - nums[i])
        dfs(0, 0)
        return self.count 